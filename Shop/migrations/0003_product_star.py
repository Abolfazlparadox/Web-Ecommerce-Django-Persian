# Generated by Django 4.2.7 on 2023-11-28 11:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0002_product_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='star',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
    ]