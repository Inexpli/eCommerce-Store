# Generated by Django 3.2.5 on 2021-08-08 16:27

import django_countries.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbase',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2),
        ),
    ]