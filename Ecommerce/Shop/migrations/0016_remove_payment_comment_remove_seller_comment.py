# Generated by Django 4.2.7 on 2023-12-09 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0015_remove_user_model_username_remove_user_model_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='comment',
        ),
    ]