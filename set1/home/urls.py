from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('course/', views.course, name="course"),
    path('course-detail/', views.courseDetail, name="course-detail"),
    path('contact/', views.contact, name="contact"),
    path('blog-single/', views.blogsingle, name='blog-single'),
    path('blog-archive/', views.blogarchive, name='blog-archive'),
    path('404-page/', views.Page404, name='404-page')
]