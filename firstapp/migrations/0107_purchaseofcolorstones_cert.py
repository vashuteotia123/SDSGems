# Generated by Django 3.2.5 on 2021-11-12 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0106_auto_20211112_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseofcolorstones',
            name='cert',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='firstapp.certificate'),
        ),
    ]