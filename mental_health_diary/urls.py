from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('disclaimer/', views.disclaimer, name='disclaimer'),
    path('self-care/', views.self_help, name='self_help'),
    path('settings/', views.settings, name='settings'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]