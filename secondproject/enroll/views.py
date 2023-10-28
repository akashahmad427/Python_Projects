from django.shortcuts import render,HttpResponseRedirect
from .forms import Fistform,Secondform,Adminform
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    if request.method == 'POST':
        fm = Fistform(request.POST)
        if fm.is_valid():
            messages.info(request,'you have been signed in successfully , ')
            fm.save()
    else:
        fm = Fistform()
    return render(request,'enroll/home.html',{'form':fm})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username = uname , password = upass)
                if user is not None:
                    login(request, user)
                    messages.info(request,'you have been login in successfully,')
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request,'enroll/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/')

def user_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.is_superuser == True:
                fm = Adminform(request.POST,instance=request.user)
                user = User.objects.all()
            else:
                fm = Secondform(request.POST,instance=request.user)
            if fm.is_valid():
                messages.info(request,'profile updated !')
                fm.save()
        else:
            if request.user.is_superuser == True:
                fm = Adminform(instance = request.user)
                user = User.objects.all()
            else:
                fm = Secondform(instance=request.user)
                user = None
        return render(request,'enroll/profile.html',{'name':request.user,'form':fm,'user':user})
    else:
        return HttpResponseRedirect('/login/')

def  user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def changepass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.info(request,'Password change successfully.')
                return HttpResponseRedirect('/profile/')
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request,'enroll/changepass.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')

def user_detail(request,id):
    if request.user.is_authenticated:
        pi = User.objects.get(pk=id)
        fm = Adminform(instance=pi)
        return render(request,'enroll/detail.html',{'form':fm})
 