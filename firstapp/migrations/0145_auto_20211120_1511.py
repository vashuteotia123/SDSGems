# Generated by Django 3.2.5 on 2021-11-20 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0144_user_table_permit_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='color_of_colorstone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'ColourStone - Color',
            },
        ),
        migrations.AlterModelOptions(
            name='color_origin',
            options={'verbose_name_plural': 'Diamonds - Color Origin'},
        ),
        migrations.AlterField(
            model_name='cloneinvofcolorstones',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='firstapp.color_of_colorstone'),
        ),
        migrations.AlterField(
            model_name='inventoryofcolorstones',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='firstapp.color_of_colorstone'),
        ),
        migrations.AlterField(
            model_name='purchaseofcolorstones',
            name='colour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='firstapp.color_of_colorstone'),
        ),
        migrations.AlterField(
            model_name='salesofcolorstones',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='firstapp.color_of_colorstone'),
        ),
    ]