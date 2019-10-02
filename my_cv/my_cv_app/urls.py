from django.urls import path

from . import views

urlpatterns = [
    path("", views.handle, name="my-cv-app"),
    path("create-test-data/", views.create_test_data, name="create-test-data")
]
