# Generated by Django 3.2.5 on 2021-10-07 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0087_auto_20211007_1208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventoryofcolorstones',
            old_name='certificate_no_cs',
            new_name='certificate_no',
        ),
        migrations.RenameField(
            model_name='purchaseofcolorstones',
            old_name='certificate_no_cs',
            new_name='certificate_no',
        ),
        migrations.RenameField(
            model_name='purchaseofcolorstones',
            old_name='purchaseapv_cs',
            new_name='purchaseapv',
        ),
        migrations.RenameField(
            model_name='purchaseofcolorstones',
            old_name='shape_cs',
            new_name='shape',
        ),
        migrations.RenameField(
            model_name='purchaseofcolorstones',
            old_name='tag_price_cs',
            new_name='tag_price',
        ),
        migrations.RenameField(
            model_name='purchaseofcolorstones',
            old_name='total_val_cs',
            new_name='total_val',
        ),
    ]
