from django.db import models

# Create your models here.


class Katalog(models.Model):
    katalog_name = models.CharField(max_length=200)

    def __str__(self):
        return self.katalog_name


class Frage(models.Model):
    LEICHT = "Leicht"
    MITTEL = "Mittel"
    SCHWER = "Schwer"
    SCHWIERIGKEITSGRAD_AUSWAHL = [
        (LEICHT, 1),
        (MITTEL, 2),
        (SCHWER, 3)
    ]
    frage = models.CharField(max_length=200)
    antwort1 = models.CharField(max_length=200)
    antwort2 = models.CharField(max_length=200)
    antwort3 = models.CharField(max_length=200)
    antwort4 = models.CharField(max_length=200)
    richtige_antwort = models.CharField(max_length=200)
    katalog = models.ForeignKey(Katalog, on_delete=models.CASCADE)
    schwierigkeitsgrad = models.CharField(
        max_length=10,
        choices=SCHWIERIGKEITSGRAD_AUSWAHL,
        default=LEICHT
    )

    def __str__(self):
        return self.frage


class User_Abs(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Teilnehmer(User_Abs):
    abgeschlossene_fragebogen = models.ManyToManyField(Frage, blank=True)


class Admin(User_Abs):
    pass


class Fragebogen(models.Model):
    fragebogen_name = models.CharField(max_length=200)
    katalog = models.ForeignKey(Katalog, on_delete=models.CASCADE)
    fragen = models.ManyToManyField(Frage, blank=True)
    teilnehmer_liste = models.ManyToManyField(Teilnehmer, blank=True)

    def __str__(self):
        return self.fragebogen_name
