# Generated by Django 3.2 on 2021-11-01 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0101_jewel_media'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryofjewellery',
            name='frontend',
            field=models.BooleanField(default=False),
        ),
    ]