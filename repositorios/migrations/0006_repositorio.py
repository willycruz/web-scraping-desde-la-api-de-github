# Generated by Django 3.0.5 on 2020-08-18 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repositorios', '0005_delete_repositorio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Repositorio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=500, null=True)),
                ('descripcion', models.CharField(max_length=500, null=True)),
                ('commits', models.CharField(max_length=20, null=True)),
                ('colaboradores', models.CharField(max_length=20, null=True)),
                ('fecha_actualizacion', models.CharField(max_length=100, null=True)),
                ('nombre_lenguajes', models.CharField(max_length=200, null=True)),
                ('url_repositorio', models.CharField(max_length=500, null=True)),
            ],
        ),
    ]
