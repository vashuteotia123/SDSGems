# Generated by Django 3.2.5 on 2021-10-07 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0091_salesofdiamond_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesofdiamond',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]