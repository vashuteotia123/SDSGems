# Generated by Django 3.2.5 on 2021-11-14 11:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0124_auto_20211114_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='cloneinvofcolorstones',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]