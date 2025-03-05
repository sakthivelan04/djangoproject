from django.urls import path
from . import views 
from events import views




urlpatterns = [
    path('cultural', views.culDetail, name='cultural'),
    path('reg',views.reg_view, name='reg'),
    path('pdf', views.cultural_pdf, name='pdf'),
    path('r', views.r, name='r'),
    path('cultural update', views.form_view, name='add'),
]
  