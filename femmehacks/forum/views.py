from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, Post, Comment
from django.contrib.auth import authenticate, login, logout

#homepage
def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')

    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('view-post/')
        else:
            return HttpResponse("Your login credentials don't match. Please try again.")

#posting page
def create_post(request):
    if request.method == 'GET':
        return render(request, 'create_post.html')

    elif request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        allow = request.POST.get('allow')
        date = request.POST.get('date')

        new_post = Post(title=title, description=description, allow_comments=allow, date=date)
        new_post.save()
        
    return redirect('/')

#viewing post page
def view_post(request):
    posts = Post.objects.all()
    return render(request, 'view_post.html', {"post_list": posts})

# page to create comments
def comment(request):
    if request.method ==  'POST':
        comment = request.POST.get('comment')
        date = request.POST.get('date')
         

#logout
def logout(request):
    logout(request)
    return redirect('/')

#signup
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        profession = request.POST.get('profession')
        field = request.POST.get('field')

        User.objects.create_user(username, password, email, profession, field)
        return redirect('view-post/')
    else:
        return render(request, 'signup.html')
    
    #user.objects.create_user ?
    


