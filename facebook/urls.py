from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('', views.login, name='login'),
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('social-auth/', include('social_django.urls', namespace='social')),
]