"""simple_votings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import handler404, handler500

from vote import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page, name='index'),
    path('registration/', views.registration_page, name='registration'),
    path('login/', views.login_page, name='login'),
    path('change_profile/', views.change_profile, name='change_profile'),
    path('add_new_voting/', views.add_new_voting, name='add_new_voting'),
    path('votes/', views.votes, name='votes'),
    path('logout/', views.logout, name='logout'),
]


handler404 = views.error_404
handler500 = views.error_500
