# Generated by Django 3.2.5 on 2021-09-28 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0053_auto_20210928_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='cloneinvofcolorstones',
            name='company_name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]