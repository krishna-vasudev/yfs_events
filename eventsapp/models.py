from django.db import models

# Create your models here.
class Events(models.Model):
    event_name = models.CharField(max_length=50)
    start_date=models.DateField()
    end_date = models.DateField()
    venue=models.TextField()
    event_description=models.TextField()
    organizer_name=models.CharField(max_length=60)
    phone_no=models.CharField(max_length=12)
    email=models.EmailField(max_length=100)
    event_activity=models.BooleanField()
    event_registration=models.BooleanField()
    reg_link=models.TextField()
    img1=models.ImageField(upload_to='images/')
    img2=models.ImageField(upload_to='images/', blank=True)
    img3=models.ImageField(upload_to='images/',blank=True)
    img4=models.ImageField(upload_to='images/',blank=True)
    img5=models.ImageField(upload_to='images/',blank=True)