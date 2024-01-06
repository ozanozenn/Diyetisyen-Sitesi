from django.shortcuts import render, redirect
from .models import Blog

def index(request):
    return render(request, 'index.html')

def index(request):
    return render(request, 'index.html')

def hakkimizda(request):
    return render(request, 'hakkimizda.html')

def hizmetler(request):
    return render(request, 'hizmetler.html')

def online_diyet(request):
    return render(request, 'online_diyet.html')


def blog(request):
     if request.method == 'POST':
          name = request.POST["name"]
          email = request.POST['email']
          message = request.POST["message"]
          contact_us = Blog(name=name,message=message,email=email)
          contact_us.save()

          return redirect('mesaj')
     else:
         return render(request,'blog.html')

def support(request):
    return render(request, 'support.html')

def tarifler(request):
    return render(request, 'tarifler.html')

def yuzyuze(request):
    return render(request, 'yuzyuze.html')

def kurumsalBeslenme(request):
    return render(request, 'kurumsalBeslenme.html')

def sporcuBeslenme(request):
    return render(request, 'sporcuBeslenme.html')

def mesaj(request):
    return render(request, 'mesaj.html')

