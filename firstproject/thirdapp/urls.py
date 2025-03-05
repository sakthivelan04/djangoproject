from django.urls import path, include
from django.views.generic import TemplateView
from . import views as v1
from . import views as v2


urlpatterns = [
    path('home/', v1.home, name='home'),
    path("signup/", v2.authView,),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', TemplateView.as_view(template_name='registration/index.html')),
]