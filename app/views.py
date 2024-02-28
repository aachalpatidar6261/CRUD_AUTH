from django.conf import settings

from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.core.mail import send_mail
#from .signals import *
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *
from .forms import TodoForm


def todo_index(request):
    #item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_index')
    else:
        item_list = Todo.objects.order_by("-date")     
    form = TodoForm()
 
    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }
     
    return render(request, 'todo_index.html', page)
 
def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('todo_index')

def index(request):
    return render(request, 'index.html')

def register(request):
    print(request.method,'request.method')
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(name=name, email=email, password=password)
        print(name,email,password)
        return redirect('login')
    
    else:        
        return render(request, 'register.html')
    
# eluj vmop kihz ypko
#@receiver(user_logged_in, sender=User)
def login(request):
    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)
        user = authenticate(email=email, password=password)
        print(user,"user", email, password)
        if user is not None:
            auth_login(request, user)
            if user.last_login is not None:  # Check if it's the first login
                print(user.last_login,"******************************")
                #send_mail(                    
                #    'Welcome to Our Site!',
                #    
                #    'Thank you for signing up! We are excited to have you as a member of our community.',
                #    'aachal.constacloud@gmail.com',
                #    [user.email],
                #    fail_silently=False,
                #)
                #return redirect('dashboard')
                subject = 'Welcome to Our Platform!'
                message = f'Hello {user.email},\n\nWelcome to our platform. We are excited to have you here!'
                sender_email = "aachal.constacloud@gmail.com"  # Update with your sender email
                recipient_email = user.email
                send_mail(subject, message, sender_email, [recipient_email])
                return redirect('dashboard')            
            return render(request,'index.html' ,{'user':user})            
        else:  
            return render(request, 'login.html', {'error_message': 'Invalid Userame or Passward'})
    else:
        return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')


####  signals.py

# from django.contrib.auth.signals import user_logged_in
# from django.dispatch import receiver
# from django.core.mail import send_mail
# #from django.contrib.auth.models import User
# from .models import *

# @receiver(user_logged_in, sender=User)
# def send_welcome_email(sender, user, request, **kwargs):
#     if user.last_login is None:  # Check if it's the first login
#         print(user.last_login,"******************************")
#         subject = 'Welcome to Our Platform!'
#         message = f'Hello {user.username},\n\nWelcome to our platform. We are excited to have you here!'
#         sender_email = "aachal.constacloud@gmail.com"  # Update with your sender email
#         recipient_email = user.email
#         send_mail(subject, message, sender_email, [recipient_email])
