# Generated by Django 4.0.2 on 2022-07-04 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artisan', '0040_alter_artisan_profession_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artisan',
            name='profession_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
