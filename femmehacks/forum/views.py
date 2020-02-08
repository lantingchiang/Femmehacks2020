from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from .models import User, Post, Comment
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError

#homepage
@csrf_exempt
def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('view-post/')
        else:
            return HttpResponse("Your login credentials don't match. Please try again.")
    else:
        return render(request, 'home.html')


#viewing post page
def view_post(request):
    posts = Post.objects.order_by('-date')[:10]
    return render(request, 'view_post.html', {"post_list": posts})


#posting page
@csrf_exempt
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        allow = request.POST.get('allow')

        new_post = Post(title=title, description=description, allow_comments=allow)
        new_post.save()
        return redirect('view-post/')
    else:
        return render(request, 'create_post.html')


#display specifics of post
def display(request, title):
    try:
        post = get_object_or_404(Post, title=title)
        return render(request, 'view_post.html', title=title)
    except Http404:
        return HttpResponse("This post does not exist.")
    

# page to create comments
@csrf_exempt
def comment(request):
    if request.method ==  'POST':
        comment = request.POST.get('comment')
        date = request.POST.get('date')
        post = request.POST.get('postname')

        new_comment = Comment(comment=comment, date=date)
        new_comment.save()

        try:
            post_instance = get_object_or_404(Post, title=post)
            new_comment.post = post_instance
            new_comment.save()
            return redirect('view-post/')

        except Http404:
            return HttpResponse("The post you're trying to comment on doesn't exist")

    else:
        return render(request, 'comment.html')


#logout
def logout(request):
    logout(request)
    return redirect('/')

#signup
@csrf_exempt
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        profession = request.POST.get('profession')
        field = request.POST.get('field')

        try:
            User.objects.create_user(username, password, email, profession=profession, field=field)
            return redirect('/')
        except IntegrityError: 
            return HttpResponse("Username already exists! Please try again!")
    else:
        return render(request, 'signup.html')
    
    #user.objects.create_user ?
    


