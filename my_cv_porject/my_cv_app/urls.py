from django.urls import path

from . import views

urlpatterns = [
    path('', views.handle, name='my-cv-app')
]