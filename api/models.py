from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Restaurant(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(max_length=360)

    def rating_count(self):
        ratings = Rating.objects.filter(resto=self)
        return len(ratings)

    def rating_avg(self):
        sum = 0
        ratings = Rating.objects.filter(resto=self)
        for rating in ratings:
            sum += rating.stars
        if len(ratings) > 0:
            return sum / len(ratings)
        else:
            return 0

class Rating(models.Model):
    resto = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = (('user', 'resto'),)
