from django.urls import path
from . import views 

# name = 'article'

urlpatterns = [
    path ('', views.main, name='main')
]