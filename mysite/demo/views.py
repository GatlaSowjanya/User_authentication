from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, "demo/home.html")


def user_register(request):
    if request.method == "GET":
        return render(request, "demo/register_page.html")
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return HttpResponse("successfully registred")
    return render(request, "demo/register.html")


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/demo/home/")
        else:
            return HttpResponse("<h1>registration is required<h1>")
    return render(request, "demo/login_page.html")


def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/demo/login/")
