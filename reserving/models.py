from pickle import FALSE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Reservations(models.Model):
    First_name = models.CharField(max_length=1000)
    Second_name = models.CharField(max_length=1000)
    Last_name= models.CharField(max_length=1000)
    Room_number = models.IntegerField()
    Amount_paid = models.IntegerField()
    Email = models.EmailField(max_length=1000)
    Occupation = models.CharField(max_length=1000)
    Nights_of_stay = models.IntegerField()
    Starting_date = models.DateField()
    Ending_date = models.DateField()
    Client = models.ForeignKey(User, unique = False, on_delete=models.CASCADE)


    def __str__(self):
        return self.First_name


