# Generated by Django 3.0.5 on 2022-01-17 07:51

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_auto_20220117_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='birthstones',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
