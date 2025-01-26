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

from django.urls import path, include
from firstapp import views
from firstapp import views as vi
from firstapp import views as v1
from firstapp import views as v2



urlpatterns = [
    
    path('cultural', views.culDetail),
    path('login',vi.clg),
    path('pdf', v1.cultural_pdf, name='pdf'),
    path('cultural update', v2.form_view, name='update'),
  path("accounts/", include("django.contrib.auth.urls")),
    
]
