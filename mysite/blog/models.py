from django.urls import reverse
from pyexpat import model
from turtle import mode

from django.db import models
from django.utils import timezone
# from django.core import reverse

# Create your models here.


class User_register(models.Model):
    username = models.CharField(max_length=200)
    useremail =models.EmailField()
    userpassword = models.CharField(max_length=50)
    

    def __str__(self):
        return self.username
        
class post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title= models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True,null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    

    def get_absolute_url(self):
        return reverse("postdetail",kwargs={'pk':self.pk}) 


    def __str__(self):
        return self.title

class Comment(models.Model):
    # post = models.ForeignKey('Post',related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text= models.TextField()
    create_date =models.DateTimeField(default=timezone.now())
    approved_comment =models.BooleanField(default=False)

    

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.text
