from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("sercat/items", views.sercat_items, name="sercat-items"),
    path("create-test-data/", views.create_test_data, name="create-test-data")
]
