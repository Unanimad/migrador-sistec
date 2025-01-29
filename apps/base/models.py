from django.db import models


class NavigationLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    url = models.TextField()
