from django.contrib import admin

# Register your models here.
from ordering import models


class ProduktAdmin(admin.ModelAdmin):
    list_display = ['name', 'preis']
    list_filter = ['preis']


admin.site.register(models.Produkt, ProduktAdmin)
admin.site.register(models.Zutaten)

# ToDo: Bestellung sollten nach Zeit filterbar sein
admin.site.register(models.Lieferung)
