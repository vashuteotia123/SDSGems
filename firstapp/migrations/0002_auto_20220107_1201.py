# Generated by Django 3.0.5 on 2022-01-07 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diamond_media',
            old_name='jewellery_info',
            new_name='diamond_info',
        ),
    ]