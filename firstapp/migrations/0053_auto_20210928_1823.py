# Generated by Django 3.2.5 on 2021-09-28 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0052_auto_20210927_1332'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cloneinvofdiamond',
            old_name='fancy_color_grade',
            new_name='fancy_color_intensity1',
        ),
        migrations.RenameField(
            model_name='cloneinvofdiamond',
            old_name='fancy_color_intensity',
            new_name='fancycolor_grade',
        ),
        migrations.RenameField(
            model_name='cloneinvofdiamond',
            old_name='white_color_grade',
            new_name='white_color_grade1',
        ),
    ]