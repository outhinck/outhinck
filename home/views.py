from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
# Create your views here.


def home(request):
    if request.method == 'POST':
        if 'Contact' in request.POST:
            try:
                name = request.POST.get('name')
                email = request.POST.get('email')
                subject = request.POST.get('subject')
                phone = request.POST.get('phone')
                message = request.POST.get('message')

                newContact = Contact(name=name,email=email,subject=subject,phone=phone,message=message)
                newContact.save()
                messages.success(request,'Successfully sent!')
            except:
                messages.error(request,'Please Try again Later.')



    return render(request,'home.html')