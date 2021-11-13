# Generated by Django 3.2 on 2021-10-19 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0097_auto_20211017_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesofjewellery',
            name='DIS',
            field=models.FloatField(default=34.55),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='salesofjewellery',
            name='DIS_amount',
            field=models.FloatField(default=34.55),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='salesofjewellery',
            name='amount',
            field=models.FloatField(default=45.66),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='salesofjewellery',
            name='currency',
            field=models.CharField(default='INR', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='salesofjewellery',
            name='gross_wt',
            field=models.FloatField(default=34.33),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='salesofjewellery',
            name='rate',
            field=models.FloatField(default=34.56),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='salesofjewellery',
            name='total_value',
            field=models.FloatField(default=345.44),
            preserve_default=False,
        ),
    ]