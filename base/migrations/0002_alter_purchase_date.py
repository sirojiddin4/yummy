# Generated by Django 4.1.4 on 2022-12-09 18:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 12, 9, 19, 1, 24, 926305)),
        ),
    ]