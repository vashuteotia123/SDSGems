# Generated by Django 3.0.5 on 2021-12-03 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0009_auto_20211203_0837'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesreturn_d',
            name='totalamount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True, verbose_name='Total Value'),
        ),
    ]