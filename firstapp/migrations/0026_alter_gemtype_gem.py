# Generated by Django 3.2.9 on 2021-12-30 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0025_alter_cloneinvofdiamond_white_color_grade1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gemtype',
            name='gem',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
