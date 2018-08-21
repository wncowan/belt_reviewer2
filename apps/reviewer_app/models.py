# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import bcrypt
from django.db import models

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = []
        if len(postData['username']) < 2:
            errors.append("name must be no fewer than 2 characters")
        if len(postData['alias']) < 1:
            errors.append("alias must be no fewer than 1 characters")
        if re.search('[0-9]', postData['alias']) != None:
            errors.append("no numbers in alias")
        if EMAIL_REGEX.match(postData['email']) == None:
            errors.append("Invalid email format")
        if len(postData['password']) < 8:
            errors.append("Password must be at least 8 characters")
        if (postData['password'] != postData['confirm_password']):
            errors.append("Password does not match Confirm Password")
        
        email_in_use = User.objects.filter(email=postData['email'])
        if email_in_use:
            print('email in use bud')
            errors.append("Email in use")
        return errors

    def login_validator(self, postData):
        errors=[]
        email_exists = User.objects.filter(email=postData['login_email'])
        print(email_exists)
        if not email_exists:
            errors.append("email is not in database. please register")
        else:
            hash1 = User.objects.filter(email=postData['login_email'])[0].password
            print(hash1)
            print(postData['login_password'])
            if not bcrypt.checkpw(postData['login_password'].encode(), hash1.encode()):
                errors.append("Incorrect Password for this user")
        return errors

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    review = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=2, decimal_places=1)

