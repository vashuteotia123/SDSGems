# Generated by Django 3.0.5 on 2022-01-12 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20220112_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='birthstones',
            name='tagline',
            field=models.CharField(max_length=300, verbose_name='Tagline'),
        ),
    ]
