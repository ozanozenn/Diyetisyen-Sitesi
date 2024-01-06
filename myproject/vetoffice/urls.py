from django.contrib import admin
from django.urls import path 
from .views import index, hakkimizda, hizmetler, online_diyet, tarifler, blog, support,yuzyuze,sporcuBeslenme ,kurumsalBeslenme,mesaj
urlpatterns = [
    path('', index, name='index'),
    path('index/', index, name='index'),
    path('hakkimizda/', hakkimizda, name='hakkimizda'),
    path('hizmetler/', hizmetler, name='hizmetler'),
    path('online_diyet/', online_diyet, name='online_diyet'),
    path('tarifler/', tarifler, name='tarifler'),
    path('blog/', blog, name='blog'),
    path('support/', support, name='support'),
    path('yuzyuze/', yuzyuze, name='yuzyuze'),
    path('kurumsalBeslenme/', kurumsalBeslenme, name='kurumsalBeslenme'),
    path('sporcuBeslenme/', sporcuBeslenme, name='sporcuBeslenme'),
    path('mesaj/', mesaj, name='mesaj'),
]
