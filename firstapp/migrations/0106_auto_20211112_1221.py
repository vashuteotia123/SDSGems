# Generated by Django 3.2.5 on 2021-11-12 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0105_auto_20211112_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cloneinvofcolorstones',
            name='Clarity',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='inventoryofcolorstones',
            name='Clarity',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseofcolorstones',
            name='Clarity',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseofcolorstones',
            name='rate',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='salesofcolorstones',
            name='Clarity',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]