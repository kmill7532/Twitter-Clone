from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,  name='index'),
    path('navbar/', views.nav,  name='navbar'),
    path('delete/<int:post_id>/', views.delete, name='delete'),
    path('home/', views.Home, name='home'),
    path('about/', views.About, name='about'),
    path('register/', views.sendMail, name='register'),
    path('like/<int:post_id>/', views.LikeView, name='like_post'),
    path('edit/<int:post_id>/', views.edit,name='edit'),
]
