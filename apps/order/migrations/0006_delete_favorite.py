# Generated by Django 5.0.4 on 2024-05-07 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_remove_cart_size'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Favorite',
        ),
    ]
