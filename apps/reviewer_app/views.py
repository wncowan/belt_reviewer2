# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.contrib import messages
from .models import User, Book
import bcrypt

def index(request):
    return render(request, "reviewer_app/login_registration.html")
    
def login(request):
    print('entered login')
    errors = User.objects.login_validator(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect('/')
    else:
        request.session['user_id'] = User.objects.filter(email=request.POST['login_email'])[0].id
        print('currently logged in:')
        print(type(request.session['user_id']))
        # return redirect('/users/' + str(request.session['user_id']))
        return redirect('/dashboard')

def create(request):
    print('entered create')
    hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect('/#toregister') 
    else:
        # new_user = User.objects.create(username=request.POST['username'], alias=request.POST['alias'], email=request.POST['email'], password=hash1, confirm_password=request.POST['confirm_password'])
        new_user = User.objects.create(username=request.POST['username'], alias=request.POST['alias'], email=request.POST['email'], password=hash1)
        request.session['user_id'] = new_user.id
        print('currently logged in: ')
        print(request.session['user_id'])
        request.session['action'] = "registered"
        print(request.session['user_id'])
        return redirect('/dashboard')

def dashboard(request):
    books = Book.objects.all()
    context = {
        "all_books": books
    }

    print("got to dboard")
    return render(request, "reviewer_app/dashboard.html", context)

def new_book(request):
    return render(request, "reviewer_app/new_book.html")

def create_book(request):
    print('added new book')
    new_book = Book.objects.create(title=request.POST['title'], author=request.POST['author'], review=request.POST['review'], rating=request.POST['rating'])
    return redirect('/dashboard')


