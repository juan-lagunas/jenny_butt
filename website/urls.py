from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.singup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('dataEntry', views.dataEntry, name='dataEntry'),
    path('addInventory', views.addInventory, name='addInventory'),
]