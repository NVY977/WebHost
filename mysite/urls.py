from django.contrib import admin
from django.urls import path, include
from todo import views


urlpatterns = [    
    path('admin/', admin.site.urls),
    path('', views.index),
    path('likes/', include('likes.urls', namespace = 'likes')),
    path('AboutUs.html', views.about),
    path('Login.html', views.login),
    path('Shop.html', views.shop),
    path('Contacts.html', views.contact),
    path('index.html', views.index),
]