# Generated by Django 3.2.5 on 2021-08-01 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0011_alter_purchaseofcolorstones_certificate_no_cs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchaseofcolorstones',
            old_name='shape',
            new_name='shape_cs',
        ),
    ]
