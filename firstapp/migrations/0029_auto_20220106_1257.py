# Generated by Django 3.0.5 on 2022-01-06 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0028_auto_20220106_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colorstone_media',
            name='stockid',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='firstapp.Inventoryofcolorstones'),
        ),
    ]
