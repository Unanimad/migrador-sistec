from django.urls import path
from .views import sistec_login

urlpatterns = [
    path('login/', sistec_login, name='sistec_login'),
]