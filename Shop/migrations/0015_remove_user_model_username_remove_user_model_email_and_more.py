# Generated by Django 4.2.7 on 2023-12-09 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0014_rename_cart_order_rename_cart_payment_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_model',
            name='Username',
        ),
        migrations.RemoveField(
            model_name='user_model',
            name='email',
        ),
        migrations.RemoveField(
            model_name='user_model',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user_model',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='user_model',
            name='password',
        ),
        migrations.RemoveField(
            model_name='user_model',
            name='password_update',
        ),
        migrations.RemoveField(
            model_name='user_model',
            name='product',
        ),
    ]
