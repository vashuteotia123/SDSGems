# Generated by Django 3.2.5 on 2021-11-17 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0127_inventoryofcolorstones_frontend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseofcolorstones',
            name='certificate_no',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]