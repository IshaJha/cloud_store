from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

# I added
from django.contrib.auth import authenticate, login
from .form import login_form
# from django.contrib.auth import authenticate, login, get_user_model, 
# Create your views here.

def log_in(request):
    context = {}
    form = login_form(request.POST or None)
    if request.method == 'POST':
        # print(request.POST)
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        print(request.user.get_username())
        # print(password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # context['message']= "Welcome to Cloud Store" + request.user.get_username()
            # A backend authenticated the credentials
            # redirect on homepage.html
            return redirect("index_home")
        else:
            context['error']= "you could not login"

    context['form']=form
    return render(request,"login.html",context)
# @login_required
# def index(request):
#     return render(request,'accounts/index.html')

def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return render(request,'accounts/index.html')
    context['form']=form
    return render(request,'registration/sign_up.html',context)

def logout_request(request):
    logout(request)
    # messages.info(request, "Logged out successfully!")
    return redirect("accounts:home")