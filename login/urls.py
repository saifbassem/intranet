from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='custom_login'),
    path('signup/', views.signup, name='custom_signup'),
    path('logout/', views.logout, name='custom_logout'),
    path('unauthorized/', views.unauthorized, name='unauthorized'),
    ]