from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

def RegisterUser(request):
    form = Register()
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'User Registered Successfully')
            return redirect('login')
    context = {
        'form':form
    }
    return render(request,'register.html',context)

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password= password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else: 
            messages.error(request,"Invalid Credentials")
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    user = request.user
    notes = Note.objects.filter(user=user)
    context = {
        "notes":notes
    }
    return render(request,'home.html',context)


@login_required(login_url='login')
def addNote(request):
    form = AddNote()
    user = request.user
    if request.method=='POST':
        form =AddNote(request.POST)
        if form.is_valid():
            form.instance.user = user
            form.save()
            return redirect('home')
    else: 
        form =AddNote()
    
    context ={
        'form' : form,
        'user': user
    }
    return render(request,'addnote.html',context)

def deleteNote(request,id):
    if request.method == 'POST':
        note = Note.objects.get(pk = id)
        note.delete()
        return redirect('home')
    
def updateNote(request,id):
    if request.method == 'POST':
        note = Note.objects.get(pk=id)
        form = AddNote(request.POST,instance = note)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        note = Note.objects.get(pk=id)
        form = AddNote(instance = note)
    context = {
        'form':form
    }

    return render(request,'note.html',context)
