from django.db import models

# Create your models here.
class Category(models.Model) :
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    create_date = models.DateTimeField('Date creation')
    update_date = models.DateTimeField('Date update')

class Size (models.Model) :
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    create_date = models.DateTimeField('Date creation')
    update_date = models.DateTimeField('Date update')

class Weight (models.Model) :
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    create_date = models.DateTimeField('Date creation')
    update_date = models.DateTimeField('Date update')

