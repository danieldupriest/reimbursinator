# Generated by Django 2.1.5 on 2019-02-01 00:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20190131_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='data_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]