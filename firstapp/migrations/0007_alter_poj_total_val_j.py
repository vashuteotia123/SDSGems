# Generated by Django 3.2.5 on 2021-07-30 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0006_auto_20210730_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poj',
            name='total_val_j',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9),
        ),
    ]
