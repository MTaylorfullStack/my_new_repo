from django.db import models
import re

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['first_name']) < 3:
            errors['name'] = "First name must be longer than 2 characters"
        if len(postData['last_name']) < 3:
            errors['lname'] = "Last name must be longer than 2 characters"
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Email is invalid"
        if len(postData['password']) < 8:
            errors['pass'] = "Password must be at least 8 characters"
        if postData['password'] != postData['confirm_password']:
            errors['pass'] = "Password and confirm password do not match"
        return errors
        


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    objects = UserManager()

class Message(models.Model):
    message = models.CharField(max_length=250)
    poster = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=
    True)

class Comment(models.Model):
    comment =  models.CharField(max_length=250)
    poster = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    message = models.ForeignKey(Message, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=
    True)

# Create your models here.
