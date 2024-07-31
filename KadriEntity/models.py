from django.db import models

class Zarplata(models.Model):
    name = models.CharField(max_length=50)
    

class Sotrudniki(models.Model):
    name = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    dateBirth = models.DateField()
   

class Dolznosty(models.Model):
    
    name = models.CharField(max_length=50)
    Sotrudniki = models.ForeignKey(Sotrudniki, on_delete = models.CASCADE)
    Zarplata = models.ManyToManyField(Zarplata)