from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from datetime import timedelta

# Create your models here.


class LoginForm(models.Model):
    username = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
    
    
class SignupForm(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    portfolio = models.URLField(max_length=255, blank=True, null=True)
    years_of_experience = models.IntegerField()
    password = models.CharField(max_length=200)
    repassword = models.CharField(max_length=200)
    profileimage = models.ImageField(
        upload_to='profilemages', null=True, default="images/user.png")
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-edited_at', '-created_at']
    
    def __str__(self):
        return self.fullname
    
    

class RecommendMaterial(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    Material_type = models.CharField(max_length=200)
    Title = models.CharField(max_length=200)
    Description = models.CharField(max_length=2000)
    Meant_for = models.CharField(max_length=2000)
    benefits_of_use = models.CharField(max_length=2000)
    Material_URL = models.URLField(max_length=200, null=True, blank=True)
    # Upload_material = models.FileField(upload_to='suggesteddocuments', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-edited_at', '-created_at']
    
    def __str__(self):
        return self.Title
    
    
    
    
class CreateRooms(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    topic = models.CharField(max_length=1000)
    # name = models.CharField(max_length=500)
    description = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    edited_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    class Meta:
        ordering = ['-edited_at', '-created_at']
    
    def __str__(self):
        return self.topic
    
    
def return_date_time():
    now = timezone.now()
    return now + timedelta(days=2)
    
class InterviewDetails(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE) 
    interviewer = models.CharField(max_length=500, null=True, blank=True)
    Date_and_time = models.DateTimeField(default=return_date_time)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    edited_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    class Meta:
        ordering = ['-edited_at', '-created_at']

    def __str__(self):
        return self.interviewer
    
    
    
class SuccessStory(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    # userdata = models.ForeignKey(SignupForm, null=True, on_delete=models.CASCADE)
    testimony = models.CharField(max_length=5000, null=True, blank=True)
    testimony = models.CharField(max_length=5000, null=True, blank=True)
    Video = models.URLField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    edited_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
        
    class Meta:
        ordering = ['-edited_at', '-created_at']

    def __str__(self):
        return self.testimony
    
class Message(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    room = models.ForeignKey(CreateRooms, null=True, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    edited_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
        
    class Meta:
        ordering = ['-edited_at', '-created_at']

    def __str__(self):
        return self.body[0:50]