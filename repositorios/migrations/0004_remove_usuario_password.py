# Generated by Django 3.0.5 on 2020-08-18 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repositorios', '0003_remove_repositorio_fecha_scraping'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='password',
        ),
    ]
