# Generated by Django 4.0.2 on 2023-05-28 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artisan', '0053_alter_bankdetails_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='artisan',
            name='years_experience',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]