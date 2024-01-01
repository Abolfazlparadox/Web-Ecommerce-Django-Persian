# Generated by Django 4.2.7 on 2023-12-02 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0010_cart_ordered'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Quantity'),
        ),
    ]
