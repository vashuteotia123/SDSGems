# Generated by Django 3.2.5 on 2021-09-28 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0065_auto_20210928_2113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cloneinvofcolorstones',
            name='units_cs',
        ),
        migrations.RemoveField(
            model_name='salesofcolorstones',
            name='units_cs',
        ),
    ]