# Generated by Django 4.0.2 on 2022-07-01 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0045_alter_serviceorder_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicerequest',
            old_name='quantity',
            new_name='number_of_workers',
        ),
    ]