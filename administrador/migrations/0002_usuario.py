# Generated by Django 3.2.7 on 2021-09-22 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=16, unique=True)),
                ('Nombre_de_usuario', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=40)),
            ],
        ),
    ]
