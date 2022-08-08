from django.urls import path

from accounts.views import user_register, user_login, user_logout
from .views import Home, ViewCar, create_car, user_personal_area, DeleteCar, EditCarView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('car/<int:pk>', ViewCar.as_view(), name='view_car'),
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('add/', create_car, name='add'),
    path('personal_area/', user_personal_area, name='personal_area'),
    path('deleteconfirmation/<int:pk>/', DeleteCar.as_view(), name='deletecar'),
    path('edit_car/<int:pk>/', EditCarView.as_view(), name='edit_car')
]
