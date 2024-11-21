from django.db import models


class Cat(models.Model):
    name = models.CharField(max_length=100)
    years_of_experience = models.PositiveIntegerField()
    breed = models.CharField(max_length=255)
    salary = models.FloatField()

    def __str__(self):
        return self.name
