# Generated by Django 3.2.5 on 2021-08-12 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
    ]