# Generated by Django 3.2.5 on 2021-08-28 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_order_authenticated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='authenticated',
        ),
    ]
