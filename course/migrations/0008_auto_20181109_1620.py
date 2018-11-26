# Generated by Django 2.0.4 on 2018-11-09 10:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_auto_20181109_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursedetails',
            name='url',
        ),
        migrations.AlterField(
            model_name='coursedetails',
            name='start_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 11, 9, 10, 50, 24, 641706, tzinfo=utc), null=True, verbose_name='Start Date'),
        ),
    ]