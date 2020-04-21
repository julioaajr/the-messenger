from app import views
from django.contrib import admin
from django.urls import path
from app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.login_user),
    path('logout/', views.logout_user),
    path('login/submit', views.submit_login),
    path('', views.index),
]
