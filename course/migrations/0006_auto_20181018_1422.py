# Generated by Django 2.1.2 on 2018-10-18 08:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_auto_20181018_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursedetails',
            name='start_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 10, 18, 8, 52, 43, 809151, tzinfo=utc), null=True, verbose_name='Start Date'),
        ),
    ]
