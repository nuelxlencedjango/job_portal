# Generated by Django 3.2 on 2022-04-23 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20220420_2210'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderitem',
            options={'ordering': ['-date_created'], 'verbose_name_plural': 'Orderitem'},
        ),
    ]
