from django.shortcuts import render, redirect
import bcrypt
from django.contrib import messages
from .models import *

def home(request):
    return render(request, 'index.html')

def register(request):
    #create a valid user
    errors = User.objects.validator(request.POST)
    print(errors)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    print(request.POST['password'])
    new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'])
    print(new_user)
    #redirect to success
    request.session['user'] = new_user.id
    return redirect('/success')

def login(request):
    logged_user = User.objects.filter(email=request.POST['email'])
    print(logged_user)
    print(logged_user[0].email)
    if len(logged_user) > 0:
        if request.POST['password'] == logged_user[0].password:
            request.session['user'] = logged_user[0].id
            return redirect('/success')
    return redirect('/')



def success(request):
    if 'user' not in request.session:
        return redirect('/')
    else:
        context = {
            'all_messages': Message.objects.all()
        }
        return render(request, "wall.html", context)


def logout(request):
    request.session.flush()
    return redirect('/')


def add_mess(request):
    print(request.POST)
    Message.objects.create(message=request.POST['content'], poster=User.objects.get(id=request.session['user']))
    return redirect('/success')

def one_user(request, user_id):
    context = {
        'my_user': User.objects.get(id=user_id)
    }
    return render(request, "profile.html", context)

def add_comm(request, mess_id):
    Comment.objects.create(comment=request.POST['content'], poster=User.objects.get(id=request.session['user']), message=Message.objects.get(id=mess_id))
    return redirect('/success')

# Create your views here.
