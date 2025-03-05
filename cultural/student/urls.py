from django.urls import path
from student import views
from django.views.generic import TemplateView
from events import views as v1

app_name = 'student'

urlpatterns = [
        path('home/', views.h, name='home'),
        path('login', views.login_view, name='login'),  # Ensure the name is 'login'
        path('logout', views.logout_view, name='logout'),
        path('register/', views.registration, name='R'),
        path('', TemplateView.as_view(template_name='culturalapp/index.html')),
]