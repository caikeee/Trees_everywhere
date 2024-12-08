# Generated by Django 5.1.4 on 2024-12-08 03:39

import datetime
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_profile_bio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='members',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='description',
        ),
        migrations.RemoveField(
            model_name='plantedtree',
            name='date_planted',
        ),
        migrations.RemoveField(
            model_name='plantedtree',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='plantedtree',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='plantedtree',
            name='plant',
        ),
        migrations.AddField(
            model_name='account',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 8, 0, 0)),
        ),
        migrations.AddField(
            model_name='plant',
            name='scientific_name',
            field=models.CharField(default='Sem nome científico', max_length=255),
        ),
        migrations.AddField(
            model_name='plantedtree',
            name='account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='planted_trees_account', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='plantedtree',
            name='age',
            field=models.IntegerField(blank=True, null=True, verbose_name='Idade'),
        ),
        migrations.AddField(
            model_name='plantedtree',
            name='planted_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='plantedtree',
            name='tree',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Ativa'),
        ),
        migrations.AlterField(
            model_name='account',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='plantedtree',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
    ]
