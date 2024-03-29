from django.shortcuts import render, redirect
from django.http import HttpResponse

def myapp_view1(request):
    return render(request, 'myapp/index.html')

def about_app(request):
    if request.method == "POST":
        return redirect('contact')
    return render(request, 'myapp/about.html')

def contact_app(request):
    if request.method == "POST":
        return redirect('home')  
    return render(request, 'myapp/contact.html')
