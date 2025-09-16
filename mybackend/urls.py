"""
URL configuration for mybackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
    # from django.contrib import admin
from django.urls import path
# from django.http import HttpResponse
from django.shortcuts import render
# from . import views

def home(request):
    return render(request, "home.html")
    # context = {"username": "Joshua"}
    # return render(request, "home.html", context)

def about(request):
    return render(request, "about.html")

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", home, name="home"),
    path("about/", about, name="about"),
]
"""
# from django.contrib import admin
# from django.http import HttpResponse
from django.urls import path
from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    submitted = False
    name = ""

    # Handle form submission
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        
        # prints it in the terminal
        print("📩 New Contact Message")
        print("Name:", name)
        print("Email:", email)
        print("Message:", message)

        submitted = True

    return render(request, "contact.html", {"submitted": submitted, "name": name})

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
]
