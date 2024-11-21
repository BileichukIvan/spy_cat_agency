from django.db import models
from cats.models import Cat


class Mission(models.Model):
    cat = models.ForeignKey(
        Cat, related_name="missions", on_delete=models.CASCADE
    )
    is_complete = models.BooleanField(default=False)
    targets = models.ManyToManyField(
        "Target", related_name="missions", blank=True
    )

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


class Target(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    notes = models.TextField()
    is_complete = models.BooleanField(default=False)
