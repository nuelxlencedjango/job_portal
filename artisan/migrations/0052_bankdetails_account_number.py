# Generated by Django 4.0.2 on 2022-07-10 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artisan', '0051_remove_bankdetails_account_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankdetails',
            name='account_number',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
