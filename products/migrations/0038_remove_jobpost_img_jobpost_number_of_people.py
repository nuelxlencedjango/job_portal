# Generated by Django 4.0.2 on 2022-06-28 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0037_jobpost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobpost',
            name='img',
        ),
        migrations.AddField(
            model_name='jobpost',
            name='number_of_people',
            field=models.IntegerField(default=1),
        ),
    ]
