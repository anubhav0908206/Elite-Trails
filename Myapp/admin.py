from django.contrib import admin
from Myapp.models import Problem
from Myapp.models import Cab
from Myapp.models import Hotel
from Myapp.models import Adventure
from Myapp.models import Custom

class ProblemAdmin(admin.ModelAdmin):
    list_display=('name','email','contact','message')

admin.site.register(Problem,ProblemAdmin)

class CabAdmin(admin.ModelAdmin):
    list_display=('name','email','contact','pickup','drop','passenger','luggage')

admin.site.register(Cab,CabAdmin)

class HotelAdmin(admin.ModelAdmin):
    list_display=('name','email','contact','beds','meals','guests','date','checkin')

admin.site.register(Hotel,HotelAdmin)

class AdventureAdmin(admin.ModelAdmin):
    list_display=('name','email','contact','emergency','location','date','person','experience')

admin.site.register(Adventure,AdventureAdmin)

class CustomAdmin(admin.ModelAdmin):
    list_display=('name','email','contact','emergency','location','date','person','destination','budget','travel','activities')

admin.site.register(Custom,CustomAdmin)
# Register your models here.


