# Generated by Django 3.2 on 2022-03-26 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artisan', '0009_alter_artisan_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artisan',
            old_name='date_joined',
            new_name='date_created',
        ),
    ]
