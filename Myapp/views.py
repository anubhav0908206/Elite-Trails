from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth, messages
from .models import Problem
from .models import Cab
from .models import Hotel
from .models import Adventure
from .models import Custom

# Create your views here.
#front index page
def index(request):
    return render(request,"index.html")

#login page
def login(request):
    if request.method == "POST":
        usern = request.POST['username']
        passn = request.POST['password']

        userm = auth.authenticate(username=usern, password=passn)

        if userm is not None:
            auth.login(request, userm)
            return redirect("explore")
        else:
            messages.info(request, "CREDENTIAL INVALID!")
            return redirect("login")

    return render(request, "login.html")

#explore page
def explore(request):
    return render(request,"explore.html")

#forget password
def forget(request):
    if request.method == "POST":
        usern = request.POST['username']
        mail = request.POST['email']
        passn = request.POST['password']
        cpassn = request.POST['cpassword']

        if passn == cpassn:

            try:
                user = User.objects.get(username=usern, email=mail)
                user.set_password(passn)
                user.save()

                messages.info(request, "Password updated successfully")
                return redirect("login")

            except User.DoesNotExist:
                messages.info(request, "User not found")
                return redirect("forget")

        else:
            messages.info(request, "Password doesn't match")
            return redirect("forget")

    return render(request, "forget_password.html")

#register password
def register(request):
    if request.method == "POST":
        usern = request.POST['username']
        mail = request.POST['email']
        passn = request.POST['password']
        cpassn = request.POST['cpassword']

        if passn == cpassn:
            if User.objects.filter(email = mail).exists():
                messages.info(request,"email already exists")
                return redirect("register")
            elif User.objects.filter(username = usern).exists():
                messages.info(request,"username already exists")
                return redirect("register")
            else:
                userapp = User.objects.create_user(username = usern, email = mail, password = passn)
                userapp.save()
                return redirect("login")
        else:
            messages.info(request,"password doesn't match")
            return redirect("register")
    else:
        return render(request,"register_user.html")
    
#about page
def about(request):
    return render(request,"about.html")

#category page
def category(request):
    return render(request,"category.html")

#form page
def form(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        message= request.POST['message']

        if name and email and contact and message:
            newdetail = Problem.objects.create(
                name=name,
                email=email,
                contact=contact,
                message=message
            )
            newdetail.save()
            messages.info(request, "Data saved successfully")
            return redirect("details")
        
    return render(request, "form.html")

#cab page
def cab(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        pickup= request.POST['pickup']
        drop= request.POST['drop']
        passenger= request.POST['passenger']
        luggage= request.POST['luggage']

        if name and email and contact and pickup and drop and passenger and luggage:
            newdetail = Cab.objects.create(
                name=name,
                email=email,
                contact=contact,
                pickup=pickup,
                drop=drop,
                passenger=passenger,
                luggage=luggage
            )
            newdetail.save()
            messages.info(request, "Data saved successfully")
            return redirect("confirm")
        
    return render(request, "cab.html")

#hotel page
def hotel(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        beds= request.POST['beds']
        meals= request.POST['meals']
        guests= request.POST['guests']
        date= request.POST['date']
        checkin=request.POST['date']

        if name and email and contact and beds and meals and guests and date and checkin:
            newdetail = Hotel.objects.create(
                name=name,
                email=email,
                contact=contact,
                beds=beds,
                meals=meals,
                guests=guests,
                date=date,
                checkin=date
            )
            newdetail.save()
            messages.info(request, "Data saved successfully")
            return redirect("confirm")
        
    return render(request, "hotel.html")

#adventure page
def adventure(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        emergency= request.POST['emergency']
        location= request.POST['location']
        date= request.POST['date']
        person= request.POST['person']
        experience=request.POST['experience']

        if name and email and contact and emergency and location and date and person and experience:
            newdetail = Adventure.objects.create(
                name=name,
                email=email,
                contact=contact,
                emergency=emergency,
                location=location,
                date=date,
                person=person,
                experience=experience
            )
            newdetail.save()
            messages.info(request, "Data saved successfully")
            return redirect("confirm")
        
    return render(request, "adventure.html")

#custom page
def custom(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        emergency= request.POST['emergency']
        location= request.POST['location']
        date= request.POST['date']
        person= request.POST['person']
        destination=request.POST['destination']
        budget=request.POST['budget']
        travel=request.POST['travel']
        activities=request.POST['activities']

        if name and email and contact and emergency and location and date and person and destination and budget and travel and activities:
            newdetail = Custom.objects.create(
                name=name,
                email=email,
                contact=contact,
                emergency=emergency,
                location=location,
                date=date,
                person=person,
                destination=destination,
                budget=budget,
                travel=travel,
                activities=activities
            )
            newdetail.save()
            messages.info(request, "Data saved successfully")
            return redirect("confirm")
        
    return render(request, "custom.html")

#confirm page
def confirm(request):
    return render(request,"confirm.html")

#details page
def details(request):
    return render(request,"details.html")