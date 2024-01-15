from django.db import models


# Create your models here.


class Movie(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=20)
    duration = models.FloatField()
    rating = models.FloatField()
    typ = models.CharField(max_length=50, default='action')
    image = models.ImageField(upload_to='Images/', default="Images/None/default.jpg")
