# Generated by Django 3.2.5 on 2021-08-04 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0021_amount_certificate_d_certificate_no_certificate_no_d_clarity_color_origin_cut_depths_dis_dis_amount_'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchaseofcolorstones',
            old_name='stockid_cs',
            new_name='stockid',
        ),
        migrations.RemoveField(
            model_name='inventoryofdiamond',
            name='stockid',
        ),
        migrations.RemoveField(
            model_name='pod',
            name='fancycolor1',
        ),
        migrations.RemoveField(
            model_name='pod',
            name='fancycolor2',
        ),
        migrations.RemoveField(
            model_name='pod',
            name='overtone',
        ),
        migrations.RemoveField(
            model_name='pod',
            name='stockid_d',
        ),
        migrations.AlterField(
            model_name='inventoryofcolorstones',
            name='stockid',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.DeleteModel(
            name='fancycolor1',
        ),
        migrations.DeleteModel(
            name='fancycolor2',
        ),
        migrations.DeleteModel(
            name='overtone',
        ),
    ]