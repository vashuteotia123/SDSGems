# Generated by Django 3.2.5 on 2021-11-23 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0150_auto_20211123_1420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colorstone_media',
            name='colorstone_info',
        ),
        migrations.RemoveField(
            model_name='colorstone_media',
            name='description',
        ),
        migrations.RemoveField(
            model_name='jewel_media',
            name='description',
        ),
        migrations.RemoveField(
            model_name='jewel_media',
            name='jewellery_info',
        ),
    ]
