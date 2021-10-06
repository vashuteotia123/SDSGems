# Generated by Django 3.2.5 on 2021-10-05 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0081_inventoryofdiamond_units'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cloneinvofdiamond',
            name='PCS_d',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cloneinvofdiamond',
            name='depth',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cloneinvofdiamond',
            name='table',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cloneinvofdiamond',
            name='units',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cloneinvofdiamond',
            name='weight_d',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='inventoryofdiamond',
            name='units',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='salesofdiamond',
            name='PCS_d',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='salesofdiamond',
            name='depth',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='salesofdiamond',
            name='table',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='salesofdiamond',
            name='units',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='salesofdiamond',
            name='weight_d',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
