# Generated by Django 5.1.4 on 2024-12-08 14:36

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_account_members_remove_plant_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('scientific_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Plant',
        ),
        migrations.RemoveField(
            model_name='account',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='joined_date',
        ),
        migrations.AddField(
            model_name='account',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='plantedtree',
            name='location_lat',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=9),
        ),
        migrations.AddField(
            model_name='plantedtree',
            name='location_long',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=9),
        ),
        migrations.AddField(
            model_name='profile',
            name='about',
            field=models.TextField(default='Sem descrição'),
        ),
        migrations.AddField(
            model_name='profile',
            name='joined',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='account',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='account',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='plantedtree',
            name='account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.account'),
        ),
        migrations.AlterField(
            model_name='plantedtree',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='plantedtree',
            name='planted_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='plantedtree',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='plantedtree',
            name='tree',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.tree'),
        ),
    ]
