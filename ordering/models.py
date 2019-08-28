from django.db import models
from django.forms import ModelForm


class Zutaten(models.Model):
    name = models.CharField(max_length=60)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Zutat"
        verbose_name_plural = "Zutaten"


class Produkt(models.Model):
    name = models.TextField()
    preis = models.DecimalField(decimal_places=2, max_digits=4)
    zutaten = models.ManyToManyField(Zutaten)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Produkt"
        verbose_name_plural = "Produkte"


class Lieferung(models.Model):
    vorname = models.CharField(max_length=50)
    nachname = models.CharField(max_length=50)
    strasse = models.CharField(max_length=60)  
    hausnummer = models.CharField(max_length=30)
    plz = models.IntegerField()
    ort = models.CharField(max_length=60)
    produkte = models.ManyToManyField(Produkt)
    ausgeliefert = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Lieferung"
        verbose_name_plural = "Lieferungen"


class LieferungForm(ModelForm):
    class Meta:
        model = Lieferung
        fields = ["produkte", "vorname", "nachname", "strasse", "hausnummer", "plz", "ort"]
        labels = None
