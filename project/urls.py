from app import views
from django.contrib import admin
from django.urls import path
from app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.login_user),
    path('logout/', views.logout_user),
    path('registrar/', views.registrar),
    path('registrar/submit', views.submit_registrar),
    path('login/submit', views.submit_login),
    path('add_friend/', views.add_friend),
    path('search/', views.search_user),
    path('del_friend/', views.del_friend),
    path('', views.index),
]
