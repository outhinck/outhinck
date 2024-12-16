from django.shortcuts import render

# Create your views here.


def home(request):
    # nothing
    return render(request,'home.html')