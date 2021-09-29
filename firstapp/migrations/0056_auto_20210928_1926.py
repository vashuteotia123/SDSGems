# Generated by Django 3.2.5 on 2021-09-28 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0055_auto_20210928_1920'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salesofcolorstones',
            old_name='clarity',
            new_name='Clarity',
        ),
        migrations.RenameField(
            model_name='salesofcolorstones',
            old_name='weight',
            new_name='Weight_cs',
        ),
        migrations.AddField(
            model_name='cloneinvofcolorstones',
            name='PCS',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cloneinvofcolorstones',
            name='Weight_cs',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inventoryofcolorstones',
            name='PCS',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inventoryofcolorstones',
            name='Weight_cs',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]