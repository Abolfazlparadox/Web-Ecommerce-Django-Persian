# Generated by Django 4.2.7 on 2023-12-05 06:10

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Shop', '0013_product_discounted_prices'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='cart',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='cart',
            new_name='order',
        ),
    ]
