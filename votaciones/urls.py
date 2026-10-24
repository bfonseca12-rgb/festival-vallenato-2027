from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('registro/', views.registro_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='votaciones/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('votar/<int:opcion_id>/', views.votar_view, name='votar'),
]