# Generated by Django 4.0.2 on 2022-07-03 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artisan', '0039_rename_order_id_viewedjob_job_order_id'),
        ('products', '0047_trainstaff'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicerequest',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='artisan.area'),
        ),
    ]
