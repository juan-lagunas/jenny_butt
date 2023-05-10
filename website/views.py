from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    if not request.user.is_authenticated:
        return render(request, 'website/nouserhome.html')
    return render(request, 'website/home.html')

def singup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmation = request.POST['confirmation']

        if not username or not email or not password or not confirmation:
            return render(request, 'website/signup.html', {
                'message': 'Must fill out all fields.'
            })
        
        if password != confirmation:
            return render(request, 'website/signup.html', {
                'message': 'Passwords do not match. Try again.'
            })
        
        if User.objects.filter(username=username):
            return render(request, 'website/signup.html', {
                'message': 'Username already taken.'
            })

        user = User.objects.create_user(username, email, password)

        user.save()

        return render(request, 'website/signin.html', {
            'message': 'Sign up sucessful'
        })
    
    return render(request, 'website/signup.html')     

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'website/signin.html', {
                'message': 'Username and password not found. Try again.'
            })
        
    return render(request, 'website/signin.html')
    

def signout(request):
    logout(request)
    return render(request, 'website/signin.html', {
        'message': 'Log out succesful.'
    })

