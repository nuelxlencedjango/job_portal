# Generated by Django 4.0.2 on 2022-07-02 15:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artisan', '0039_rename_order_id_viewedjob_job_order_id'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0046_rename_quantity_servicerequest_number_of_workers'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainStaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('type_of_service', models.CharField(blank=True, max_length=200, null=True)),
                ('number_of_people', models.IntegerField(default=1)),
                ('status', models.CharField(blank=True, default='Pending', max_length=200, null=True)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('date_created', models.DateField(auto_now_add=True, null=True)),
                ('work_done', models.BooleanField(default=False, null=True)),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='artisan.area')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'TrainStaff',
                'ordering': ['-date_created'],
            },
        ),
    ]
