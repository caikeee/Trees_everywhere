# Generated by Django 5.1.4 on 2024-12-08 15:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_plantedtree_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plantedtree',
            name='account',
        ),
        migrations.AlterField(
            model_name='plantedtree',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='plantedtree',
            name='location_lat',
            field=models.DecimalField(decimal_places=6, max_digits=9),
        ),
        migrations.AlterField(
            model_name='plantedtree',
            name='location_long',
            field=models.DecimalField(decimal_places=6, max_digits=9),
        ),
        migrations.AlterField(
            model_name='plantedtree',
            name='tree',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tree'),
        ),
    ]