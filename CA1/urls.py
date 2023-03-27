"""CA1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from django.urls.conf import include
from django.views.generic.base import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("guitar_shop.urls")),  #Includes the URLs of guitar_shop in the main project
    path("accounts/", include("accounts.urls")),     #To include th urls of accounts/urls.py in the project
    path("accounts/", include("django.contrib.auth.urls")),  #Includes the auth app, which adds some authentification features to the project
    path('', TemplateView.as_view(template_name='home.html'), name='home'),     #To register the home page
    
]
