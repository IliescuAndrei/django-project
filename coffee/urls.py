from django.urls import path
from coffee import views
from coffee.views import LoginView, RegisterView, LogoutView

urlpatterns = [
    path("", views.cafea_index, name="cafea_index"),
    path("<int:pk>/", views.cafea_detail, name="cafea_detail"),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]