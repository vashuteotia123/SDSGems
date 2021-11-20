# Generated by Django 3.2.5 on 2021-11-20 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0139_auto_20211119_2109'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=30)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='firstapp.countries')),
            ],
        ),
    ]