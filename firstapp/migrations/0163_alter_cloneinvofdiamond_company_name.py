# Generated by Django 3.2.9 on 2021-11-30 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0162_alter_salesofdiamond_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cloneinvofdiamond',
            name='company_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='firstapp.companyinfo'),
        ),
    ]
