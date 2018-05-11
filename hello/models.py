from django.db import models

class Timeline(models.Model):
    user_name = models.CharField(max_length=20, help_text="Enter your full name")
