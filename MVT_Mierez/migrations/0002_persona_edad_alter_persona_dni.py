# Generated by Django 4.1 on 2022-08-22 19:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MVT_Mierez', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='edad',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(105), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='persona',
            name='dni',
            field=models.CharField(max_length=8),
        ),
    ]
