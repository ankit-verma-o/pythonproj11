# Generated by Django 3.0 on 2019-12-09 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0008_auto_20191209_0329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sightings',
            name='Date',
            field=models.DateField(blank=True, help_text='Date', null=True),
        ),
    ]
