# Generated by Django 2.2.4 on 2019-08-21 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produkt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('preis', models.DecimalField(decimal_places=4, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Zutaten',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Lieferung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strasse', models.TextField()),
                ('plz', models.IntegerField()),
                ('produkte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordering.Produkt')),
            ],
        ),
    ]
