from django.db import models


# Create your models here.

class Katalog(models.Model):
    katalog_name = models.CharField(max_length=200)

    def __str__(self):
        return self.katalog_name


class Frage(models.Model):    
    frage = models.CharField(max_length=200)
    antwort = models.CharField(max_length=200, blank=True)    
    richtige_antwort = models.CharField(max_length=200)
    
    def __str__(self):
        return self.frage


class Fragebogen(models.Model):
    fragebogen_name = models.CharField(max_length=200)
    katalog = models.ForeignKey(Katalog, on_delete=models.CASCADE)
    fragen = models.ManyToManyField(Frage, blank=True)    

    def __str__(self):
        return self.fragebogen_name