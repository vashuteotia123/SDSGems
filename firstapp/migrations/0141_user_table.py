# Generated by Django 3.2.5 on 2021-11-20 07:23

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0140_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email_id', models.EmailField(max_length=254)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('fax', models.CharField(blank=True, max_length=100, null=True)),
                ('Businesstype', models.CharField(choices=[('Customer', 'Customer'), ('Wholesaler', 'Wholesaler'), ('Broker', 'Broker')], default='Customer', max_length=30)),
                ('address1', models.CharField(max_length=30)),
                ('address2', models.CharField(blank=True, max_length=30, null=True)),
                ('city', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=100)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='firstapp.countries')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='firstapp.state')),
            ],
        ),
    ]