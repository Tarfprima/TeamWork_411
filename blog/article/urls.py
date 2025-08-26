from django.urls import path
from . import views 



app_name = 'article'


urlpatterns = [
    path('', views.post_list, name='post_list'),
    # path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/<int:uid>/', views.profile, name='profile'),
    path('posts/new/', views.post_form, name='post_form'),
]