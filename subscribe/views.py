from django.shortcuts import render,redirect
from .models import Subscribe
from .forms import SubscribeForm
# from django.urls import reverse

def subscribe(request):
    form = SubscribeForm()
    if request.method== 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():

            #CLASS FORM
            # first_name = form.cleaned_data['first_name']  # [] is used because it get as dictionarty and first_name is the key
            # last_name = form.cleaned_data['last_name']
            # email = form.cleaned_data['email']
            # obj = Subscribe(first_name=first_name, last_name=last_name, email=email)
            # obj.save()
            # return redirect('thankyou')

            #MODEL FORM
            form.save()
            return redirect('thankyou')
    context = {
        'form':form,
    }
    return render(request,'subscribe.html',context)

def thankyou(request):
    return render(request,"thankyou.html")
