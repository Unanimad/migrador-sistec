from django.urls import path, include

from apps.base.views import index

urlpatterns = [
    path('', index, name='index'),
    path('sistec/', include('apps.sistec.urls'), name='sistec'),
]
