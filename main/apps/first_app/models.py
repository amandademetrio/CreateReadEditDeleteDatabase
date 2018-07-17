from django.db import models
import re
from django.contrib import messages

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def basic_validator(self,postData):
        errors = {}
        #Checking for length
        if len(postData['first_name']) < 2:
            errors['first_name_len'] = "First name should have at least 2 characters"
        if len(postData['last_name']) < 2:
            errors['last_name_len'] = "Last name should have at least 2 characters"
        if len(postData['email']) < 2:
            errors['email_len'] = "Email should have at least 2 characters"
        #Making sure names are only letters
        if not postData['first_name'].isalpha():
            errors['first_name_alpha'] = "First name must contain only letters"
        if not postData['last_name'].isalpha():
            errors['last_name_alpha'] = "Last name must contain only letters"
        #Making sure email matches format
        if not EMAIL_REGEX.match(postData['email']):
            errors['email_format'] = "Invalid email format"
        #Making sure email isn't already in the list
        if User.objects.filter(email=postData['email']):
            errors['already_registered'] = "Email is already in the database" 
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()