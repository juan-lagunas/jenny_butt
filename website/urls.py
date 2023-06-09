from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.singup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('dataEntry', views.dataEntry, name='dataEntry'),
    path('addInventory', views.addInventory, name='addInventory'),
    path('inventory', views.inventory, name='inventory'),
    path('logs', views.log, name='logs'),
    path('checkout', views.checkout, name='checkout'),
]