from django.db import models
from django.db.models.query import QuerySet

# Create your models here.

class poll(models.Model):
    Question = models.TextField()
    option_one = models.models.CharField( max_length=40)
    option_two = models.models.CharField( max_length=40)
    option_three = models.models.CharField( max_length=40)
    option_four = models.models.CharField( max_length=40)
    option_five = models.models.CharField( max_length=40)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)
    option_four_count = models.IntegerField(default=0)
    option_five_count = models.IntegerField(default=0)

