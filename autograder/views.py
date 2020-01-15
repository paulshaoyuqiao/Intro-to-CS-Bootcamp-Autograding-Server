from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from .forms import SignUpForm
from subprocess import check_output
from os import remove
from os.path import join, abspath
from .test_generator import TestRunner, assignment_by_method

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    return render(request, 'signup.html')

def logout_view(request):
    logout(request)
    return home(request)

def attempt_create(request):
    if request.method == 'POST':
        new_username = request.POST['username']
        new_password = request.POST['password']
        new_email = request.POST['email']
        try:
            user = User.objects.create_user(new_username, new_email, new_password)
        except IntegrityError:
            # user already exists, throws integrity error
            return render(signup, 'signup.html', context={'exists': True})
        else:
            # successfully created the new user
            user.save()
            return render(request, 'home.html', context={'user_created': True})
    return HttpResponseRedirect('/signup')

def attempt_login(request):
    if request.method == 'POST':
        login_username = request.POST['username']
        login_password = request.POST['password']
        user = authenticate(username=login_username, password=login_password)
        if user is not None:
            # redirect to the assignment submission page
            return render(request, 'score.html', context={'username': login_username})
        else:
            # authentication failed
            return render(request, 'home.html', context={'failedlogin': True})

def handle_submission(request):
    if request.method == 'POST':
        file_list = request.FILES.getlist('code')
        content = ''
        for file in file_list:
            assignment_name = assignment_by_method[file.name[:-3]]
            target_path = allocate_temp_location_for_file(file, assignment_name)
            output = TestRunner.run_tests(assignment_name)
            content += str(output)
        # clear out the temp file to save storage
        try:
            remove(target_path)
        except OSError:
            pass
        return HttpResponse(content)
    return home(request)

def allocate_temp_location_for_file(file, assignment):
    # reallocate the mem-cached file into temp storage for executing on the server
    target_path = './grading_scripts/{}/{}'.format(assignment, file.name)
    try:
        remove(target_path)
    except OSError:
        pass
    with open(target_path, 'wb+') as dest:
        for chunk in file.chunks():
            dest.write(chunk)
    return target_path
