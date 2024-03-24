

from django.urls import path
from main import views
app_name='main'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('show/<int:car_id>/', views.show, name='show'), 
    path('rent/<str:car_name>/', views.rent_car, name='rent_car'),
    path('success/', views.success_page, name='success_page'),
]
