from django.db import models

# Create your models here.

class cardata(models.Model):
    name=models.CharField(max_length=25)
    image=models.ImageField(upload_to='pix')
    dis=models.TextField()

