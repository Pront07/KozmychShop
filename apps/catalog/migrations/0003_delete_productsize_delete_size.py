# Generated by Django 5.0.4 on 2024-05-06 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_size_productsize'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductSize',
        ),
        migrations.DeleteModel(
            name='Size',
        ),
    ]
