# Generated by Django 5.0.4 on 2024-05-07 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_favorite'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Favorite',
        ),
    ]