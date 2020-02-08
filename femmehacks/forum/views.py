from django.shortcuts import render, redirect
from django.http import HttpResponse

#homepage
def home(request):
    return HttpResponse("Homepage")

#posting page
def create_post(request):
    return HttpResponse("create_psot")

#viewing post page
def view_post(request):
    return HttpResponse("view_post")

#login
def login(request):
    return HttpResponse("login")

#logout
def logout(request):
    return HttpResponse("logout")

#signup
def signup(request):
    return HttpResponse("signup")


