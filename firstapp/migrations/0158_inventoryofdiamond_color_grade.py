# Generated by Django 3.2.9 on 2021-11-30 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0157_auto_20211129_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryofdiamond',
            name='color_grade',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
