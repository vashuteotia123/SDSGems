# Generated by Django 3.0.5 on 2022-01-06 06:29

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('user', '0009_auto_20220102_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
