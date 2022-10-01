from django.urls import path
from car.views import *

urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('about/', About.as_view(), name='about'),
    path('add_car/', AddCar.as_view(), name='add_car'),
    path('', Connect.as_view(), name='connect'),
    path('brand_cars/<slug:car_slug>', BrandCars.as_view(), name='brand_cars'),
    path('one_car/<slug:one_car_slug>', OwnerCar.as_view(), name='owner_car'),
    path('about_car/<slug:about_car_slug>', AboutCar.as_view(), name='about_car'),
    path('about_one_car/<int:about_one_car_id>', AboutOneCar.as_view(), name='about_one_car'),
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]