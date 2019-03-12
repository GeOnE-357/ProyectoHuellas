# Generated by Django 2.1.1 on 2019-03-12 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fisico',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='infocomp',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='persona',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='fisico',
            name='modified',
        ),
        migrations.RemoveField(
            model_name='infocomp',
            name='modified',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='modified',
        ),
        migrations.AddField(
            model_name='fisico',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='infocomp',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
