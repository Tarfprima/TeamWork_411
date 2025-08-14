from django.db import models

class Artile(models.Model):
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=100000)
    date = models.DateTimeField(auto_now_add=True)



