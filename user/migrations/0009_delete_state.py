# Generated by Django 3.0.5 on 2022-01-12 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_remove_user_table_state'),
    ]

    operations = [
        migrations.DeleteModel(
            name='State',
        ),
    ]
