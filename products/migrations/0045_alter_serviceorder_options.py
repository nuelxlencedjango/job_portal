# Generated by Django 4.0.2 on 2022-07-01 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0044_remove_cart_items_remove_cart_products_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='serviceorder',
            options={'ordering': ['-ordered_date'], 'verbose_name_plural': 'ServiceOrder'},
        ),
    ]
