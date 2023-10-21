from django.db import models
from datetime import datetime


class Item(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    staff_name = models.CharField(max_length=100)
    position = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    year_joined = models.IntegerField()  # or a similar numeric field type

