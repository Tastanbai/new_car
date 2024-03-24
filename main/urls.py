
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from main import views
app_name='main'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('show/<int:car_id>/', views.show, name='show'), 
     path('rent/<int:car_id>/<str:car_name>/', views.rent_car, name='rent_car'),
    path('success/', views.success_page, name='success_page'),
    path('return_car/<int:car_id>/', views.return_car, name='return_car'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)