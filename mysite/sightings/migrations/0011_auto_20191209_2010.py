# Generated by Django 3.0 on 2019-12-09 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0010_auto_20191209_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sightings',
            name='X',
            field=models.FloatField(help_text='Latitude'),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Y',
            field=models.FloatField(help_text='Longitude'),
        ),
    ]
