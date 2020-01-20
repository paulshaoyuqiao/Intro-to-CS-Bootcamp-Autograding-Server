from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .forms import SignUpForm
from subprocess import check_output
from os import remove
from os.path import join, abspath
from .test_generator import TestRunner, assignment_by_method
from .models import Submission, Assignment

# Create your views here.
def home(request):
    return render(request, 'home.html')


def signup(request):
    return render(request, 'signup.html')


@login_required(login_url='/')
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
        request.user = authenticate(username=login_username, password=login_password)
        if request.user is not None:
            # redirect to the assignment submission page
            return render(request, 'score.html', context={'username': login_username})
            # return display_scores(request, login_username)
        else:
            # authentication failed
            return render(request, 'home.html', context={'failedlogin': True})


def handle_submission(request):
    if request.method == 'POST':
        file_list = request.FILES.getlist('code')
        contents = []
        for file in file_list:
            assignment_name = assignment_by_method[file.name[:-3]]
            target_path = allocate_temp_location_for_file(file, assignment_name)
            summary, output = TestRunner.run_tests(assignment_name)
            contents.append(output)
        # clear out the temp file to save storage
        try:
            remove(target_path)
        except OSError:
            pass
        target_assignment = Assignment.objects.get(name__exact=assignment_name)
        actual_score = summary.get('total_full_score', 0)
        percentage = round(actual_score / summary.get('actual_full_score', -1), 2)
        target_submission = Submission.objects.create(
            kind=assignment_name[:-1],
            submitted_by=request.user.get_username(),
            assignment=target_assignment,
            score=actual_score,
            percentage="{}%".format(str(percentage * 100))
        )
        target_submission.save()
        return render(request, 'result.html', context={'summary': summary, 'contents': contents})
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
