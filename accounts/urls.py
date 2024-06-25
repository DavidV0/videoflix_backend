from django.urls import path
from .views import RegisterView, LoginView, home

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('', home, name='home'),
]
