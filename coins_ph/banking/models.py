from django.db import models

# Create your models here.
class Account(models.Model):
    user_id = models.IntegerField()
    currency = models.TextField(max_length=10)
    balance = models.FloatField()
    active = models.BooleanField()

class Payment(models.Model):
    account = models.IntegerField()
    to_account = models.IntegerField()
    direction = models.TextField(max_length=20)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

class User(models.Model):
    name = models.TextField(max_length=100)
    username = models.TextField(max_length=100)
    active = models.BooleanField()
