# Generated by Django 5.0.4 on 2024-05-06 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_cart_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='size',
        ),
    ]
