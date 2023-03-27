from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.adminindex, name='adminindex'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('retrievedata/', views.retrievedata, name='retrievedata'),
    path('usertable/', views.usertable, name='usertable'),
    path('memberlogin/', views.memberlogin, name='memberlogin'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    # path('takedata/', views.takedata, name='takedata'),
]