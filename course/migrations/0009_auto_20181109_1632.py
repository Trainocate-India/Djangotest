# Generated by Django 2.0.4 on 2018-11-09 11:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_auto_20181109_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursedetails',
            name='url',
            field=models.SlugField(default=1, help_text='a user friendly url', max_length=60, verbose_name='user friendly url'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='coursedetails',
            name='start_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 11, 9, 11, 2, 33, 122373, tzinfo=utc), null=True, verbose_name='Start Date'),
        ),
    ]