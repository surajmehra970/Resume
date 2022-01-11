from django.shortcuts import render
from django.contrib import messages
from .form import contactf

def resume(request):
    return render(request, 'home.html')

def skill(request):
    return render(request, 'skill.html')

def contact(request):
    if request.method == 'POST':
        form = contactf(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submission successful')
            form = contactf()
    else:
        form = contactf()
    return render(request, 'contact.html', {'form':form})

def project(request):
    return render(request, 'project.html')
    