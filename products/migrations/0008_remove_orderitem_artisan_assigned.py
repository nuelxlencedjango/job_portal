# Generated by Django 3.2 on 2022-04-20 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20220420_1142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='artisan_assigned',
        ),
    ]