# Generated by Django 3.2.5 on 2021-08-07 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0027_auto_20210807_2104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dis_amount',
            name='amount',
        ),
        migrations.AddField(
            model_name='dis_amount',
            name='disamount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='dis',
            name='dis',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
