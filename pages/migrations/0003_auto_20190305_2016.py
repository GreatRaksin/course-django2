# Generated by Django 2.1.7 on 2019-03-05 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20190305_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=500, null=True, unique=True, verbose_name='URL'),
        ),
    ]
