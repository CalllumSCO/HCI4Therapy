from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('disclaimer/', views.disclaimer, name='disclaimer'),
    path('self-care/', views.self_help, name='self_help'),
    path('settings/', views.settings, name='settings'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='main/logout.html'), name='logout'),
    path('new-entry/', views.new_entry, name='new_entry'),
    path('new-article/', views.new_article, name='new_article'),
    path('entry/<str:entry_slug>/', views.view_entry, name='view_entry'),
    path('edit-entry/<str:entry_slug>/', views.edit_entry, name='edit_entry'),

]