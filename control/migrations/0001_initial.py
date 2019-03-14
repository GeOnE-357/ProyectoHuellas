# Generated by Django 2.1.1 on 2019-03-14 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=20)),
                ('accion', models.CharField(max_length=20)),
                ('tabla', models.CharField(max_length=20)),
                ('objeto', models.IntegerField()),
                ('fecha', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'control_logs',
            },
        ),
    ]
