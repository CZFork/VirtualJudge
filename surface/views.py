from django.shortcuts import render


# Create your views here.

def problems(request):
    return render(request, 'problems.html')


def problem(request):
    return render(request, 'problem.html')


def submissions(request):
    return render(request, 'submissions.html')


def register(request):
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')
