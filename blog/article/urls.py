from django.urls import path
from . import views 


app_name = 'article'

urlpatterns = [
    path ('', views.main, name='main'),
    path ('register/', views.register, name='register'),
    path ('login/', views.login, name='login'),
    path ('posts/', views.post_list, name='posts'),
    path ('new/', views.post_form, name='new'),
]