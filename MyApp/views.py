from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import JobPost

def index(request):
    jobs = JobPost.objects.all()
    context = {
        'jobs':jobs,
    }
    return render(request,'index.html',context)


def job_detail(request,id):
    job = JobPost.objects.get(id=id)
    context = {
        'job':job
    }
    return render(request,'jobdetails.html',context)