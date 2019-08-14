from django.contrib import admin
from django.urls import path
from cool_app import views

urlpatterns = [
    path('result', views.result, name='result'),
    path('', views.test, name='first_page'),
    path('test', views.test, name='test'),
    path('admin/', admin.site.urls),
]
