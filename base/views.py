from django.shortcuts import render

from base.models import Subject

# Create your views here.


def home(request):
    subjects = Subject.objects.all()

    print(subjects[0].topics)

    context = {
        'subjects': subjects,
    }

    return render(request, 'base/home.html', context)


def subject(request, title):
    subject = Subject.objects.get(title=title)

    context = {
        'subject': subject,
    }

    return render(request, 'base/subject.html', context)
