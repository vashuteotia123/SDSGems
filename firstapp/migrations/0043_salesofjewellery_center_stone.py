# Generated by Django 3.2.5 on 2021-08-23 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0042_remove_salesofjewellery_center_stone'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesofjewellery',
            name='center_stone',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]