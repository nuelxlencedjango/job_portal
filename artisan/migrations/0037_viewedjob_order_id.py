# Generated by Django 3.2 on 2022-04-30 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artisan', '0036_viewedjob_work_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='viewedjob',
            name='order_id',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
