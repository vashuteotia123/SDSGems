# Generated by Django 3.2.5 on 2021-11-14 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0116_purchaseofcolorstones_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesofcolorstones',
            name='comment',
            field=models.TextField(blank=True, max_length=3000, null=True),
        ),
    ]