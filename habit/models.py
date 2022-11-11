from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    description = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-created']
    def __str__(self):
        return self.user.username + " - " + self.name


class Daily(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True) 

    class Meta:
        verbose_name_plural = "Daily habit"

    def __str__(self):
        return str(self.habit) + " - " + str(self.date)

