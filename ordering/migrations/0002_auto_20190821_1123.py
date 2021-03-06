# Generated by Django 2.2.4 on 2019-08-21 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lieferung',
            options={'verbose_name': 'Liefrung', 'verbose_name_plural': 'Lieferungen'},
        ),
        migrations.AlterModelOptions(
            name='produkt',
            options={'verbose_name': 'Produkt', 'verbose_name_plural': 'Produkte'},
        ),
        migrations.AlterModelOptions(
            name='zutaten',
            options={'verbose_name': 'Zutat', 'verbose_name_plural': 'Zutaten'},
        ),
        migrations.AlterField(
            model_name='produkt',
            name='preis',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
