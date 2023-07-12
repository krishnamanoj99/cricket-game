"""
URL configuration for myGame project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from game import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.store_data, name='store_data'),
    path('about/', views.about_view, name='about'),
    path('about/', views.about_view, name='about'),
    path('rules/', views.rules_view, name='rules_view'),
    path('toss/', views.toss_view, name='toss_view'),
    path('batting_first/', views.batting_first_view, name='batting_first_view'),
    path('bowling_first/', views.bowling_first_view, name='bowling_first_view'),
    path('batting_second/', views.batting_second_view, name='batting_second_view'),
    path('bowling_second/', views.bowling_second_view, name='bowling_second_view'),
    path('result/', views.result_view, name='result_view')
]
