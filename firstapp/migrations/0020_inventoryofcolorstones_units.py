# Generated by Django 3.0.5 on 2021-12-09 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0019_auto_20211209_0758'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryofcolorstones',
            name='units',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
