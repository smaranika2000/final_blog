from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    image = models.ImageField(upload_to='shop/images', default="")
    option = models.CharField(max_length=50, default='abc')
    city = models.CharField( max_length=50)
    state= models.CharField( max_length=50,default='SOME STRING')
    pincode = models.IntegerField()

    def __str__(self):
        return self.user.username


class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    image = models.ImageField(upload_to='shop/images', default="")
    category=models.CharField(max_length=255)
    summary=models.CharField(max_length=500)
    content=models.TextField()
    author=models.CharField(max_length=14)
    slug=models.CharField(max_length=130)
    draft=models.CharField(max_length=255)
    def __str__(self):
        return self.category
    class Meta:
        db_table = "Post"

class confApt(models.Model):
    required_specialist = models.CharField(max_length=50)
    apointment_date = models.DateField(auto_now=False, auto_now_add=False)
    appointment_stime = models.TimeField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.apointment_date
    class Meta:
        db_table = "confApt"

