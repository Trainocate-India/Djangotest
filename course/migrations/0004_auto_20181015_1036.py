# Generated by Django 2.1.2 on 2018-10-15 05:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20181009_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursecontent',
            name='sub_title',
            field=models.CharField(max_length=100, verbose_name='Sub title'),
        ),
        migrations.AlterField(
            model_name='coursedetails',
            name='start_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 10, 15, 5, 6, 27, 531707, tzinfo=utc), null=True, verbose_name='Start Date'),
        ),
    ]