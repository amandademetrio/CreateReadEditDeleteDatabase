from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from .models import *

def index(request):
    context = {
        "users":User.objects.all()
    }
    return render(request,'first_app/users.html',context)

def new(request):
    return render(request,'first_app/usersaddnew.html')

def show(request,number):
    context = {
        'user_to_be_shown':User.objects.get(id=number)
        }
    return render(request,'first_app/usersdisplay.html',context)

def edit(request,number):
    context = {
        'user_to_be_edited':User.objects.get(id=number)
    }
    return render(request,'first_app/usersedit.html',context)

def create(request):
    errors = User.objects.basic_validator(request.POST)

    if len(errors):
        for key,value in errors.items():
            messages.error(request,value)
        return redirect('/users/new')
    
    else:
        new_user = User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'])
        new_user.save()
        id = new_user.id
        return redirect(show, number=id)   

def destroy(request,number):
    user_to_be_deleted = User.objects.get(id=number)
    user_to_be_deleted.delete()
    return redirect('/users')

def update(request):
    user_id = request.POST['user_id']
    current_user = User.objects.get(id=user_id)
    errors = User.objects.basic_validator(request.POST)

    if len(errors):
        for key,value in errors.items():
            messages.error(request,value)
        return redirect(edit,number=user_id)

    else:
        current_user.first_name=request.POST['first_name']
        current_user.last_name=request.POST['last_name']
        current_user.email=request.POST['email']
        current_user.save()
        return redirect(show, number=user_id) 