from django.db import models

class Timeline(models.Model):
    title = models.CharField(max_length=100, help_text="Timeline title")
    memories = models.ForeignKey('Memories', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title


class Memories(models.Model):
    title = models.CharField(max_length=100, help_text="Memory name")
    entry = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title

class User(models.Model):
    time_line = models.ForeignKey('Timeline', on_delete=models.CASCADE)
    user_name = models.CharField(max_length=20, help_text="Enter your full name")

    def __str__(self):
        return self.title

