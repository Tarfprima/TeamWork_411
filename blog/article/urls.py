from django.urls import path
from . import views 


# name = 'article'

urlpatterns = [
    path ('', views.main, name='main'),
    path ('register/', views.register, name='register'),
    path ('login/', views.login, name='login'),
]