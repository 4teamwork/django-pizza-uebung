from django.db import models
from django.forms import ModelForm


class Zutaten(models.Model):
    name = models.CharField(max_length=60)
    # ToDo: Produkt Übersicht einfügen
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Zutat"
        verbose_name_plural = "Zutaten"


class Produkt(models.Model):
    name = models.TextField()
    preis = models.DecimalField(decimal_places=2, max_digits=4)
    # ToDo: Ich will wissen, was für Zutaten in Produkt sind

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Produkt"
        verbose_name_plural = "Produkte"


class Lieferung(models.Model):
    strasse = models.CharField(max_length=60)  # ToDo: Strassennummer einzeln erfassen
    plz = models.IntegerField()
    ort = models.CharField(max_length=60)
    produkte = models.ManyToManyField(Produkt)
    # ToDo: Name von Kunde wird nicht erfasst
    # ToDo: Lieferung muss abschliessbar sein

    class Meta:
        verbose_name = "Lieferung"
        verbose_name_plural = "Lieferungen"


class LieferungForm(ModelForm):
    class Meta:
        model = Lieferung
        fields = ["produkte", "strasse", "plz", "ort"]
        labels = None
