from django.urls import path
from .views import sistec_login

app_name = 'sistec'

urlpatterns = [
    path('login/', sistec_login, name='login'),
]
