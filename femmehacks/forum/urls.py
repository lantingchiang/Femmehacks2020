from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-post', views.create_post, name='create-post'),
    path('view-post', views.view_post, name='view-post'),
    path('display', views.display, name='display'),
    path('comment', views.comment, name='comment'),
    path('accounts/logout', views.logout_func, name='logout'),
    path('accounts/signup', views.signup, name='signup'),
]