# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200)),
                ('contenido', models.TextField()),
                ('slug', models.SlugField(unique=True, max_length=200)),
                ('publico', models.BooleanField(default=True)),
                ('creado', models.DateField(auto_now_add=True)),
                ('modificado', models.DateField(auto_now=True)),
            ],
        ),
    ]
