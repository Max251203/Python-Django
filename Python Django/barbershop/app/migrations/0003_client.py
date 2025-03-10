# Generated by Django 5.0 on 2023-12-27 23:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_shift'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('barber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.barber')),
                ('shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.shift')),
            ],
        ),
    ]
