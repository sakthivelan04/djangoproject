"""
URL configuration for firstproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from secondapp import views
from django.views.generic import TemplateView
from firstapp import views as v1

app_name = 'secondapp'

urlpatterns = [
        path('home', views.h, name='home'),
        path('login', views.login_view, name='login'),  # Ensure the name is 'login'
        path('logout', views.logout_view),
        path('register', views.registration),
        path('', TemplateView.as_view(template_name='culturalapp/index.html')),
]
