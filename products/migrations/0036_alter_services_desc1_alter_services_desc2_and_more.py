# Generated by Django 4.0.2 on 2022-06-25 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0035_services'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='desc1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='desc2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='desc3',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='service_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
