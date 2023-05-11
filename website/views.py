from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Category, Part, Inventory, Log
from datetime import datetime

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
            'message': 'Sign up successful'
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
        'message': 'Log out successful.'
    })


# Handle inputing data into parts,subcategory,category databases
def dataEntry(request):
    if request.method == 'POST':
        # Set variables for user input
        form_category = request.POST['category'].title()
        form_part = request.POST['part'].title()
        try:
            form_price = float(request.POST['price'])
        except ValueError:
            return render(request, 'website/home.html', {
                'message2': 'Not a valid price'
            })

        # If any input field not filled out return error message
        if not form_category or not form_part or not form_price:
            return render(request, 'website/home.html', {
                'message2': 'Please Fill Out Fields.'
            })
        
        # Get category data using user's input
        category_data = Category.objects.filter(category=form_category)
        if category_data.exists():
            if Part.objects.filter(name=form_part).exists():
                return render(request, 'website/home.html', {
                    'message2': 'Part already exists'
                })
            else:
                Part.objects.create(
                    name=form_part,
                    price=form_price,
                    category=category_data.first()
                )
        else:      
            try: 
                Category.objects.create(category=form_category)
                Part.objects.create(
                    name=form_part,
                    price=form_price,
                    category=category_data.first()
                )
            except:
                return render(request, 'website/home.html', {
                    'message2': 'Part name already taken. Must be unique.'
                })

        return render(request, 'website/home.html', {
            'message2': 'Data entry successful!'
        })


# Handle adding parts into inventory database
def addInventory(request):
    if request.method == 'POST':
        # Store user input and confirm input for quantity is a whole number
        form_part = request.POST['part'].title()
        try:
            form_quantity = int(request.POST['quantity'])
        except ValueError:
            return render(request, 'website/home.html', {
                'message1': 'Not a valid number.'
            })
        
        # Check that both fields were filled
        if not form_part or not form_quantity:
            return render(request, 'website/home.html', {
                'message1': 'Please Fill Out Fields.'
            })
        
        # Check that part exists in Parts database
        try:
            part_data = Part.objects.get(name=form_part)
        except:
            return render(request, 'website/home.html', {
                'message1': 'Part not found'
            })
        
        # Using part data get subcategory data
        category_data = Category.objects.get(category=part_data.category)
        date = datetime.now()

        # If part exists in Inventory database update quantity else put part in database
        if Inventory.objects.filter(name=part_data.name).exists():
            inventory_data = Inventory.objects.get(name=part_data.name)
            inventory_data.quantity += form_quantity
            inventory_data.save()
        else:
            Inventory.objects.create(
                category=category_data.category,
                name=part_data.name,
                quantity=form_quantity,
                price=part_data.price,
            )

        # Create a new log for the update of Inventory
        Log.objects.create(
            category=category_data.category,
            name=part_data.name,
            quantity=form_quantity,
            price=part_data.price,
            time=date,
        )

        return render(request, 'website/home.html', {
            'message1': 'Inventory entry was successful'
        })
    

def inventory(request):
    inventory = Inventory.objects.all()
    total = 0
    for part in inventory:
        row_total = part.price * part.quantity
        total += row_total


    return render(request, 'website/inventory.html', {
        'inventory': inventory,
        'total': f'{total:.2f}',
    })

def log(request):
    logs = Log.objects.all()
    return render(request, 'website/logs.html', {
        'logs': logs
    })

def checkout(request):
    pass
