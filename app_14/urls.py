from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('adminlogin/', views.adminlogin, name= 'adminlogin'),
    path('adminpage/', views.adminpage, name= 'adminpage'),
    path('recipe/', views.recipe, name= 'recipe'),
    path('getdata/', views.getdata, name='getdata'),
    path('table/', views.table, name='table'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('adminlogout/', views.adminlogout, name= 'adminlogout'),
    path('receivedata/', views.receivedata, name = 'receivedata'),
    path('message/', views.message, name = 'message'),
    path('viewrecipe/', views.viewrecipe, name='viewrecipe'),
    path('eachrecipe/<int:id>/', views.eachrecipe, name='eachrecipe'),
]
