from django.db import models

# Create your models here.

class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=500)
    title_content = models.TextField(max_length=5000, default=True)
    content = models.TextField(max_length=5000)
    date = models.DateField(auto_now=True)
    author = models.CharField(max_length=300)
    img=models.ImageField(upload_to='Travel', default='default_image.jpg')

    def __str__(self):
        return self.title
    
