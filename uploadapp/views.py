from django.shortcuts import render
from . forms import UploadForm, UploadFileForm
from django.http import HttpResponse

def upload(request):
    form = UploadForm()
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            saved_img = form.instance   # this step is to show the image after uploading (not important)
            return render(request,'upload.html',{'form':form,'saved_img':saved_img})
    else:
        form = UploadForm()
    return render(request,'upload.html',{'form':form})



def uploadfile(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            saved_file = form.instance   # this step is to show the file after uploading (not important)
            return render(request,'file.html',{'form':form,'saved_file':saved_file})
        else:
            return HttpResponse('failed')
            
    form = UploadFileForm()
    return render(request,'file.html',{'form':form})