# Generated by Django 3.2.5 on 2021-10-05 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0076_alter_cloneinvofcolorstones_measurements'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesofcolorstones',
            name='measurements',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
