# Generated by Django 3.0.5 on 2022-01-17 07:49

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_auto_20220116_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='birthstones',
            name='description',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='birthstones',
            name='name',
            field=models.CharField(max_length=300, verbose_name='Stone Name'),
        ),
    ]
