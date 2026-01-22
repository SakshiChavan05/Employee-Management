from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    mobile=models.CharField(max_length=10)
    salary=models.IntegerField()
    position=models.CharField(max_length=50)
