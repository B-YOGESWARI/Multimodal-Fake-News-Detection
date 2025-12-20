from django.db import models

class RegisteredUser(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class PredictionHistory(models.Model):
    username = models.CharField(max_length=100)
    text = models.TextField()
    image = models.CharField(max_length=200)
    result = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username