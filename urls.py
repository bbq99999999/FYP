"""travel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from django.urls import path
from .views import index, login, register, contact, explore, listing, single_listing, pay

from django.conf.urls.static import static
from django.conf import settings
import os

urlpatterns = [
    path('index/', index, name='index'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('contact/', contact),
    path('explore/', explore),
    path('listing/', listing),
    path('single_listing/', single_listing),
    path('pay/', pay),
]
