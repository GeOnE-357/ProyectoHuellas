# Generated by Django 2.1.1 on 2019-03-11 18:00

from django.db import migrations, models
import django.db.models.deletion
import persona.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BarbaBigote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barba_bigote', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BocaContorno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contorno', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BocaEspesor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('espesor', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CabelloColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CabelloLargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('largo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CejaDireccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CejaPilosidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pilosidad', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EstadoCivil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Fisico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('altura', models.FloatField(max_length=10)),
                ('peso', models.FloatField(max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(null=True)),
                ('barba_bigote', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='persona.BarbaBigote')),
                ('boca_contorno', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='persona.BocaContorno')),
                ('boca_espesor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='persona.BocaEspesor')),
                ('cabello_color', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='persona.CabelloColor')),
                ('cabello_largo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='persona.CabelloLargo')),
                ('ceja_direccion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='persona.CejaDireccion')),
                ('ceja_pilosidad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='persona.CejaPilosidad')),
            ],
        ),
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('cara', models.FileField(upload_to=persona.models.directorio)),
                ('frente', models.FileField(upload_to=persona.models.directorio)),
                ('izquierda', models.FileField(upload_to=persona.models.directorio)),
                ('atras', models.FileField(upload_to=persona.models.directorio)),
                ('derecha', models.FileField(upload_to=persona.models.directorio)),
            ],
        ),
        migrations.CreateModel(
            name='InfoComp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ocupacion', models.CharField(blank=True, max_length=100)),
                ('nombre_padre', models.CharField(max_length=100)),
                ('padre_vive', models.BooleanField(blank=True, default=True)),
                ('nombre_madre', models.CharField(max_length=100)),
                ('madre_vive', models.BooleanField(blank=True, default=True)),
                ('conyugue', models.CharField(blank=True, max_length=100)),
                ('conyugue_vive', models.BooleanField(blank=True, default=True)),
                ('telefono', models.BigIntegerField(blank=True)),
                ('celular', models.BigIntegerField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(null=True)),
                ('estado_civil', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='persona.EstadoCivil')),
            ],
        ),
        migrations.CreateModel(
            name='ManoDeUso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uso', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Menton',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forma', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Nariz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forma', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OjoColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OjoForma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forma', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OjoTono',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tono', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registro', models.IntegerField()),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('apellido2', models.CharField(blank=True, max_length=100)),
                ('apodo', models.CharField(blank=True, max_length=100)),
                ('domicilio', models.CharField(max_length=100)),
                ('domicilio_laboral', models.CharField(blank=True, max_length=100)),
                ('fnac', models.DateField()),
                ('dni', models.BigIntegerField()),
                ('nacionalidad', models.CharField(max_length=100)),
                ('provincia', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=100)),
                ('lugar_residencia', models.CharField(blank=True, max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sexo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Tez',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='persona',
            name='sexo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='persona.Sexo'),
        ),
        migrations.AddField(
            model_name='infocomp',
            name='id_persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persona.Persona'),
        ),
        migrations.AddField(
            model_name='foto',
            name='id_persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persona.Persona'),
        ),
        migrations.AddField(
            model_name='fisico',
            name='id_persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persona.Persona'),
        ),
        migrations.AddField(
            model_name='fisico',
            name='mano_de_uso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='persona.ManoDeUso'),
        ),
        migrations.AddField(
            model_name='fisico',
            name='menton',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='persona.Menton'),
        ),
        migrations.AddField(
            model_name='fisico',
            name='nariz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='persona.Nariz'),
        ),
        migrations.AddField(
            model_name='fisico',
            name='ojo_color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='persona.OjoColor', verbose_name='Color de Ojos'),
        ),
        migrations.AddField(
            model_name='fisico',
            name='ojo_forma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='persona.OjoForma', verbose_name='Forma de Ojos'),
        ),
        migrations.AddField(
            model_name='fisico',
            name='ojo_tono',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='persona.OjoTono', verbose_name='Tono de Ojos'),
        ),
        migrations.AddField(
            model_name='fisico',
            name='tez',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='persona.Tez', verbose_name='Color de Piel'),
        ),
    ]
