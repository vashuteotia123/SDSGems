# Generated by Django 3.2.5 on 2021-08-07 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0028_auto_20210807_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poj',
            name='discount',
            field=models.DecimalField(blank=True, decimal_places=2, default=1, max_digits=9),
            preserve_default=False,
        ),
    ]
