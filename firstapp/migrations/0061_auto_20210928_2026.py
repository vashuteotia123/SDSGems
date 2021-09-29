# Generated by Django 3.2.5 on 2021-09-28 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0060_alter_purchaseofcolorstones_weight_cs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchaseofcolorstones',
            old_name='purchaseapvcs',
            new_name='purchaseapv_cs',
        ),
        migrations.RemoveField(
            model_name='inventoryofcolorstones',
            name='weight',
        ),
        migrations.AlterField(
            model_name='inventoryofcolorstones',
            name='Weight_cs',
            field=models.FloatField(null=True),
        ),
    ]
