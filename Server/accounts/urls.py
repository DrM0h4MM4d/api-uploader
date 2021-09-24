from django.urls import path
from . import views

 
urlpatterns = [
    path('register/', views.UserRegistrationApiView.as_view(), name='register'),
    path('admin/crud/', views.UsersRetrieveUpdateDestroyApiView.as_view(), name='admin-crud'),
]
