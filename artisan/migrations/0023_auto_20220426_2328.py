# Generated by Django 3.2 on 2022-04-26 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artisan', '0022_auto_20220425_1403'),
    ]

    operations = [
        migrations.RenameField(
            model_name='viewedjob',
            old_name='date_vewd',
            new_name='accepted',
        ),
        migrations.AddField(
            model_name='viewedjob',
            name='date_accepted',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
