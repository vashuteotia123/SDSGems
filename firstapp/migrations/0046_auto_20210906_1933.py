# Generated by Django 3.2.5 on 2021-09-06 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0045_remove_poj_stockid'),
    ]

    operations = [
        migrations.AddField(
            model_name='cloneinvofjewellery',
            name='salesapprovalstatus',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='salesofjewellery',
            name='salesapprovalstatus',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
