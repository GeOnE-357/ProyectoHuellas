# Generated by Django 2.1.1 on 2019-03-13 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('incidente', '0002_auto_20190313_1713'),
    ]

    operations = [
        migrations.RenameField(
            model_name='distintivo',
            old_name='parte_id',
            new_name='parte',
        ),
        migrations.RenameField(
            model_name='incidente',
            old_name='calzado_id',
            new_name='calzado',
        ),
        migrations.RenameField(
            model_name='incidente',
            old_name='persona_id',
            new_name='persona',
        ),
        migrations.RenameField(
            model_name='incidente',
            old_name='tipo_id',
            new_name='tipo',
        ),
        migrations.RenameField(
            model_name='partefoto',
            old_name='distintivo_id',
            new_name='distintivo',
        ),
    ]
