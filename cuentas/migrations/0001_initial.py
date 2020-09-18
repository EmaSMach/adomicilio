# Generated by Django 3.1.1 on 2020-09-14 05:41

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Domicilio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provincia', models.CharField(blank=True, max_length=80, null=True)),
                ('ciudad', models.CharField(blank=True, max_length=100, null=True)),
                ('barrio', models.CharField(blank=True, max_length=100, null=True)),
                ('calle', models.CharField(blank=True, max_length=100, null=True)),
                ('numero_calle', models.IntegerField(blank=True, null=True)),
                ('manzana', models.IntegerField(blank=True, null=True)),
                ('parcela', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('numero_telefono', models.CharField(blank=True, max_length=13, null=True)),
                ('domicilio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='people', to='cuentas.domicilio')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]