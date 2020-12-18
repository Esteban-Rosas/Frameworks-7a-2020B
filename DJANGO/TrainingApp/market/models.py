from django.db import models

# Create your models here.

class Category(models.Model) :
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    create_date = models.DateTimeField('Date creation')
    update_date = models.DateTimeField('Date update')

class Seller(models.Model) :
    code = models.CharField(max_length=1000)
    name = models.CharField(max_length=100)
    age = models.IntegerField(max_length=30)

class Buyers(models.Model) :
    code = models.CharField(max_length=1000)
    name = models.CharField(max_length=100)
    age = models.IntegerField(max_length=30)
    city = models.CharField(max_length=50)

class Admin(models.Model) :
    code = models.CharField(max_length=1000)
    name = models.CharField(max_length=100)
    age = models.IntegerField(max_length=30)
    status = models.BooleanField(default=True)
    create_date = models.DateTimeField('Date creation')
    update_date = models.DateTimeField('Date update')      