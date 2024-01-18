# Generated by Django 4.2.5 on 2024-01-18 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0012_remove_profile_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='predio',
            name='departamento',
        ),
        migrations.RemoveField(
            model_name='predio',
            name='distrito',
        ),
        migrations.RemoveField(
            model_name='predio',
            name='lote',
        ),
        migrations.RemoveField(
            model_name='predio',
            name='manzana',
        ),
        migrations.RemoveField(
            model_name='predio',
            name='provincia',
        ),
        migrations.RemoveField(
            model_name='predio',
            name='sector',
        ),
        migrations.AddField(
            model_name='predio',
            name='ubicacion',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]