# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.commons.utils.validators
import django.contrib.auth.models
import django.utils.timezone
from django.conf import settings
import django.core.validators
import apps.users.models.User


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('avatar', models.ImageField(null=True, upload_to=apps.users.models.User.download_loc, blank=True)),
                ('telephone', models.CharField(max_length=12, verbose_name='Tel\xe9fono', validators=[django.core.validators.RegexValidator(b'^[0-9]*$', b'solo se permite ingresar numeros.'), django.core.validators.MinLengthValidator(4), django.core.validators.MaxLengthValidator(12)])),
                ('cellphone', models.CharField(max_length=12, verbose_name='Celular', validators=[django.core.validators.RegexValidator(b'^[0-9]*$', b'solo se permite ingresar numeros.'), django.core.validators.MinLengthValidator(4), django.core.validators.MaxLengthValidator(12)])),
                ('dni', models.CharField(max_length=8, verbose_name='DNI', validators=[apps.commons.utils.validators.validate_dni])),
                ('birth_date', models.DateField(null=True, verbose_name='Fecha de nacimiento', blank=True)),
                ('gender', models.IntegerField(blank=True, null=True, verbose_name='Sexo', choices=[(1, 'Hombre'), (2, 'Mujer')])),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'users',
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'default_permissions': (),
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('store_name', models.CharField(max_length=80, verbose_name='Nombre de la tienda')),
                ('telephone', models.CharField(max_length=60, null=True, verbose_name='Tel\xe9fono', blank=True)),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='Correo electr\xf3nico', blank=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo', choices=[(True, 'Activo'), (False, 'No Activo')])),
                ('user', models.ManyToManyField(related_name='users', verbose_name='Usuarios', to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
                'db_table': 'store',
                'verbose_name': 'Tienda',
                'verbose_name_plural': 'Tiendas',
            },
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together=set([('email',)]),
        ),
    ]
