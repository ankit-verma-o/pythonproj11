# Generated by Django 3.0 on 2019-12-09 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0005_auto_20191209_0304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sightings',
            name='Date',
            field=models.CharField(blank=True, help_text='Date', max_length=10, null=True),
        ),
    ]
