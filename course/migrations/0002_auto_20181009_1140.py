# Generated by Django 2.0.4 on 2018-10-09 06:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursedetails',
            name='start_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 10, 9, 6, 10, 5, 115974, tzinfo=utc), null=True, verbose_name='Start Date'),
        ),
    ]
