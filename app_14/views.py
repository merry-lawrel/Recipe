from django.shortcuts import render,redirect
from .models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.

def adminlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['uname'] = username
            request.session['psword'] = password
            return redirect('adminpage')
        else:
            return render(request,'adminlogin.html', {'msg':'Sorry Invalid User Credentials'})
    else:
        return render(request, 'adminlogin.html')

def adminlogout(request):
    return redirect('adminlogin')

def adminpage(request):
    return render(request, 'adminpage.html')


def recipe(request):
    return render(request, 'recipe.html')

def getdata(request):
    if request.method == 'POST':
        name1 = request.POST['recipe_name']
        img1 = request.FILES['recipe_image']
        ing = request.POST['ingredients']
        ins = request.POST['instructions']
        data = Sample(recipe_name = name1, recipe_image = img1, ingredients = ing, instructions = ins)
        data.save()
        return redirect('/table')

def table(request):
    data = Sample.objects.all()
    return render(request, 'table.html', {'data':data})

def edit(request,id):
    data = Sample.objects.filter(id=id)
    return render(request, 'edit.html', {'data':data})

def update(request,id):
    if request.method == 'POST':
        name1 = request.POST['recipe_name']
        try:
            img_c = request.FILES['recipe_image']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file = Sample.objects.get(id=id).recipe_image
        ing = request.POST['ingredients']
        ins = request.POST['instructions']
        Sample.objects.filter(id=id).update(recipe_name = name1, recipe_image = file, ingredients = ing, instructions = ins)
        return redirect('/table')

def delete(request,id):
    data = Sample.objects.filter(id=id).delete()
    return redirect('/table')

def receivedata(request):
    if request.method == 'POST':
        nm = request.POST['name']
        em = request.POST['email']
        sb = request.POST['subject']
        mg = request.POST['message']
        data1 = Simple(name = nm, email = em, subject = sb, message = mg)
        data1.save()
        return redirect('/')

def message(request):
    data1 = Simple.objects.all()
    return render(request, 'message.html', {'data':data1})


def viewrecipe(request):
    data = Sample.objects.all()
    return render(request, 'viewrecipe.html', {'data':data})

def eachrecipe(request,id):
    data3 = Sample.objects.filter(id=id)
    return render(request, 'eachrecipe.html', {'data':data3})