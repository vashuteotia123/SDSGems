# Generated by Django 3.0.5 on 2022-01-07 05:02

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import taggit.managers
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='countries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Subscribed_users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=90)),
            ],
        ),
        migrations.CreateModel(
            name='User_table',
            fields=[
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email_id', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('fax', models.CharField(blank=True, max_length=100, null=True)),
                ('Businesstype', models.CharField(choices=[('Customer', 'Customer'), ('Wholesaler', 'Wholesaler'), ('Broker', 'Broker')], default='Customer', max_length=30)),
                ('address1', models.CharField(max_length=30)),
                ('address2', models.CharField(blank=True, max_length=30, null=True)),
                ('city', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=100)),
                ('permit_user', models.BooleanField(default=False)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.countries')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.State')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog_images/')),
                ('title', models.CharField(max_length=30)),
                ('subject', tinymce.models.HTMLField(blank=True, null=True)),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]
