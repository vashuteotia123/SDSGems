# Generated by Django 3.2.5 on 2021-11-14 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0117_salesofcolorstones_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesofcolorstones',
            name='PCS',
            field=models.IntegerField(null=True, verbose_name='Pieces'),
        ),
    ]
