from django.contrib import admin
from django.urls import path
from cool_app import views

urlpatterns = [
    path('', views.my_site, name='home'),
    path('me', views.about, name='me'),
    path('admin/', admin.site.urls)
]
