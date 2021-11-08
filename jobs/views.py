from django.shortcuts import render
from .models import Job


def home(request):
    
    return render(request, 'jobs/home.html')


def about(request):
    
    return render(request, 'jobs/about.html')


def home1(request):
    return render(request, 'jobs/home1.html')


def projects(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/projects.html', {'jobs':jobs})

# def jobs(request):
#     jobs = Job.objects.all()
#     return render(request, 'jobs/home.html', {'jobs':jobs})