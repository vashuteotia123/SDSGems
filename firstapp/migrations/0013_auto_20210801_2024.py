# Generated by Django 3.2.5 on 2021-08-01 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0012_rename_shape_purchaseofcolorstones_shape_cs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseofcolorstones',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='purchaseofcolorstones',
            name='total_val_cs',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True),
        ),
    ]