from django.urls import path
from . import views 


<<<<<<< HEAD
app_name = 'article'

urlpatterns = [
    path ('', views.main, name='main'),
    path ('register/', views.register, name='register'),
    path ('login/', views.login, name='login'),
    path ('posts/', views.post_list, name='posts'),
    path ('new/', views.post_form, name='new'),
=======

app_name = 'article'


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('posts/new/', views.post_create, name='post_create'),
>>>>>>> b05ce96d636ac492de9c171c06a58d5394bee828
]