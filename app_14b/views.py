from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def adminindex(request):
    return render(request, 'adminindex.html')

def about(request):
    return render(request, 'about.html')
    
def contact(request):
    return render(request, 'contact.html')

def register(request):
    return render(request, 'register.html')

def retrievedata(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pword = request.POST['password']
        flname = request.POST['fullname']
        mail = request.POST['e_mail']
        phn = request.POST['phone']
        data2 = Registerdb(username = uname, password = pword, fullname = flname, email = mail, phone = phn)
        data2.save()
        return redirect('adminindex')

def usertable(request):
    data2 = Registerdb.objects.all()
    return render(request, 'usertable.html', {'data':data2})

# def takedata(request):
#     if request.method == 'POST':
#         unm = request.POST['username']
#         psw = request.POST['password']
#         if Registerdb.objects.filter(username=unm, password = psw):
#             return redirect('/')
#         else:
#             return render(request,'login.html', {'msg':'Sorry Invalid User Credentials'})
#     else:
#             return render(request,'login.html')

def login(request):
     return render(request, 'login.html')

def memberlogin(request):
    if request.method == "POST":
        username_r = request.POST.get('username')
        password_r = request.POST.get('password')
        if Registerdb.objects.filter(username=username_r,password=password_r).exists():
            data = Registerdb.objects.filter(username=username_r,password=password_r).values('username','password','fullname','email','phone','id').first()
            request.session['uname'] = data['username']
            request.session['psword'] = data['password']
            request.session['fname'] = data['fullname']
            request.session['mail'] = data['email']
            request.session['mob'] = data['phone']
            request.session['username'] = username_r
            request.session['password'] = password_r
            request.session['uid'] = data['id']
            return redirect('adminindex')
        else:
            return render(request,'login.html', {'msg': 'Sorry, Invalid user credentials'})
    else:
        return render(request, 'login.html')

def logout(request):
    del request.session['uname']
    del request.session['psword']
    del request.session['fname']
    del request.session['mail']
    del request.session['mob']    
    del request.session['uid']
    return redirect('adminindex')

