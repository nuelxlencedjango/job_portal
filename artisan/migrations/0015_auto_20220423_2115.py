# Generated by Django 3.2 on 2022-04-23 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artisan', '0014_viewedjob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viewedjob',
            name='category',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='viewedjob',
            name='description',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='viewedjob',
            name='job_name',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
