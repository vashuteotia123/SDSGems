# Generated by Django 3.2.5 on 2021-10-06 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0082_auto_20211006_0015'),
    ]

    operations = [
        migrations.AddField(
            model_name='cloneinvofdiamond',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='inventoryofdiamond',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pod',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
