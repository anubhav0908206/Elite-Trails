from django.urls import path
from . import views
urlpatterns=[
    path("",views.index,name="index"),

    path("login",views.login,name="login"),
    path("register",views.register,name="register"),
    path("forget",views.forget,name="forget"),

    path("explore",views.explore,name="explore"),

    path("about",views.about,name="about"),
    
    path("category",views.category,name="category"),

    path("form",views.form,name="form"),

    path("cab",views.cab,name="cab"),

    path("hotel",views.hotel,name="hotel"),

    path("adventure",views.adventure,name="adventure"),

    path("custom",views.custom,name="custom"),

    path("confirm",views.confirm,name="confirm"),

    path("details",views.details,name="details"),
]