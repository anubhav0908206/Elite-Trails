from django.db import models

class Problem(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False,help_text="Enter your name ")
    email = models.EmailField(max_length=254, unique=False, help_text="Enter your valid email ")
    contact = models.CharField(max_length=10, help_text="Enter your 10 digits phone number")
    message=models.TextField(help_text="Enter about the problem you faced")

class Cab(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False,help_text="Enter your name ")
    email = models.EmailField(max_length=254, unique=False, help_text="Enter your valid email ")
    contact = models.CharField(max_length=10, help_text="Enter your 10 digits phone number")
    pickup=models.CharField(max_length=1000, null=False, blank=False,help_text="Enter your Pickup loaction")
    drop=models.CharField(max_length=1000, null=False, blank=False,help_text="Enter your Drop loaction")
    passenger = models.CharField(max_length=10, help_text="Enter your No of Passenger")
    luggage = models.CharField(max_length=8, help_text="Enter luggage you carry")

class Hotel(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False,help_text="Enter your name ")
    email = models.EmailField(max_length=254, unique=False, help_text="Enter your valid email ")
    contact = models.CharField(max_length=10, help_text="Enter your 10 digits phone number")
    beds=models.CharField(max_length=4, null=False, blank=False,help_text="Enter your Number of beds you want")
    meals = models.CharField(max_length=50) 
    date = models.DateField()  
    guests= models.CharField(max_length=10, help_text="Enter your No of guests")
    checkin = models.DateField(help_text="Enter your check-in date")

class Adventure(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False,help_text="Enter your name ")
    email = models.EmailField(max_length=254, unique=False, help_text="Enter your valid email ")
    contact = models.CharField(max_length=10, help_text="Enter your 10 digits phone number")
    emergency = models.CharField(max_length=10, help_text="Enter 10 digits  emergency phone number")
    location = models.CharField(max_length=50, help_text="Enter the prefered location") 
    date = models.DateField()  
    person= models.CharField(max_length=10, help_text="Enter your No of person")
    experience= models.CharField(max_length=10, help_text="Enter your Experience level")

class Custom(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False,help_text="Enter your name ")
    email = models.EmailField(max_length=254, unique=False, help_text="Enter your valid email ")
    contact = models.CharField(max_length=10, help_text="Enter your 10 digits phone number")
    emergency = models.CharField(max_length=10, help_text="Enter 10 digits  emergency phone number")
    location = models.CharField(max_length=50, help_text="Enter the prefered location") 
    date = models.DateField()  
    person= models.CharField(max_length=10, help_text="Enter your No of person")
    destination= models.CharField(max_length=10, help_text="Enter your choice")
    budget=models.CharField(max_length=10, help_text="Enter your budget")
    travel=models.CharField(max_length=100, null=False, blank=False,help_text="Enter your travel prefrence ")
    activities=models.CharField(max_length=10, help_text="Enter your choice")
# Create your models here.
