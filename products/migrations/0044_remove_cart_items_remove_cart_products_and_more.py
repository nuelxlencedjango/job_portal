# Generated by Django 4.0.2 on 2022-06-29 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0043_rename_product_postjob_services'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='items',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='products',
        ),
        migrations.DeleteModel(
            name='PaidServices',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
