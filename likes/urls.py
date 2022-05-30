from django.urls import path
from .views import post_view, like_post
from todo import views
app_name = 'posts'

urlpatterns = [
  path('', post_view, name='post-list'),
  path('likes/', like_post, name='like-post'), #Нужно для поиска страницы по пути
  path('AboutUs.html', views.about),
  path('Login.html', views.login),
  path('Shop.html', views.shop),
  path('Contacts.html', views.contact),
  path('index.html', views.index)
]