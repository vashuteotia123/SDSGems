# Generated by Django 3.0.5 on 2021-12-09 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0020_inventoryofcolorstones_units'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseofcolorstones',
            name='discount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True),
        ),
    ]