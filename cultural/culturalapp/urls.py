from django.urls import path, include
from django.views.generic import TemplateView
from . import views as v1
from . import views as v2
from . import views as v3
from student import views
urlpatterns = [
    path('register/', views.registration, name='R'),
    path('logout', views.logout_view, name='l'),
    path('index/', views.h, name='r'),
    path('home/', v1.home, name='h'),
    path("user signup/", v2.authView, name="signup"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("event/", v3.culDetail, name='event'),
    path('update/', TemplateView.as_view(template_name='culturalapp/index.html')),
] 