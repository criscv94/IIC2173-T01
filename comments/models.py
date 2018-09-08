from django.db import models


class Comment(models.Model):
    """Model for comments"""
    request_time = models.DateTimeField()
    request_ip = models.CharField(max_length=200)
    message = models.CharField(max_length=254)
