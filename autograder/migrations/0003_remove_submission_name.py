# Generated by Django 3.0.2 on 2020-01-20 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autograder', '0002_remove_assignment_due_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='name',
        ),
    ]
