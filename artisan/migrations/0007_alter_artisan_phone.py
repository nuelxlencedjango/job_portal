# Generated by Django 3.2 on 2022-03-26 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artisan', '0006_auto_20220325_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artisan',
            name='phone',
            field=models.CharField(max_length=15, null=True, unique=True),
        ),
    ]
