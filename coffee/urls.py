from django.urls import path
from . import views

urlpatterns = [
    path("", views.cafea_index, name="cafea_index"),
    path("<int:pk>/", views.cafea_detail, name="cafea_detail"),
]