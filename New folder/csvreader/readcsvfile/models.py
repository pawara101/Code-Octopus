from django.db import models

# Create your models here.
class Item(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    staff_name = models.CharField(max_length=100)
    position = models.CharField(max_length=200)
    age = models.IntegerField()
    year_joined = models.IntegerField(max_length=4)  # or a similar numeric field type    