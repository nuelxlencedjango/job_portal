# Generated by Django 4.0.2 on 2022-06-29 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0042_remove_postjob_job_title_postjob_paid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postjob',
            old_name='product',
            new_name='services',
        ),
    ]
