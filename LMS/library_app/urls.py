from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.home),
    path('available_books/', views.available_books, name='available_books'),
    path('contact_us/', views.contact_us, name="contact_us"),
    path('authors/',views.authors, name="authors"),
    path('about_us/', views.about_us, name="about_us"),
    path('privacy_policy/', views.privacy_policy, name="privacy_policy"),
    path('terms/', views.terms, name="terms"),

]
