"""
Definition of urls for FilmenGunea.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/',
         LoginView.as_view(
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context={
                 'title': 'Log in',
                 'year': datetime.now().year,
             },
             success_url='/logged'
         ),
         name='login'),
    path('logged/', views.logged, name='logged'),
    path('filmakikusi/', views.filmakikusi, name='filmakikusi'),
    path('bozkatu/', views.bozkatu, name='bozkatu'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]

