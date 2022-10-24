from email.policy import default
from pyexpat import model
from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    pass

class Profile:
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField()
    last_name = models.CharField()

# Create your models here.
class Habit(models.Model):
    title = models.CharField(default="My habit")
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    positive = models.BooleanField(default=True)

class HabitLog(models.Model):
    