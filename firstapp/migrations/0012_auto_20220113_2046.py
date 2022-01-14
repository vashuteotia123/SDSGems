# Generated by Django 3.0.5 on 2022-01-13 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0011_auto_20220113_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poj',
            name='center_stone',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='firstapp.centerstone'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='poj',
            name='color_of_center_stone',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='firstapp.colorofcstone'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='poj',
            name='jewellery',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='firstapp.jewell'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='poj',
            name='metal',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='firstapp.metal1'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='poj',
            name='shape',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='firstapp.shape1'),
            preserve_default=False,
        ),
    ]