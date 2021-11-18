from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    uploaded_at=models.DateTimeField(default=datetime.now,blank=True)
    body=RichTextField(blank=True,null=True)
    blog_image=models.ImageField(upload_to='blog_images/')
    blog_views=models.IntegerField(default=0)
    no_of_likes=models.IntegerField(default=0)
    no_of_comments=models.IntegerField(default=0)

class Comment(models.Model):
    parent_blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    reader=models.ForeignKey(User,on_delete=models.CASCADE)
    commented_at=models.DateTimeField(default=datetime.now,blank=True)
    body=models.TextField(blank=True)

class Like(models.Model):
    parent_blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    reader = models.ForeignKey(User, on_delete=models.CASCADE)
