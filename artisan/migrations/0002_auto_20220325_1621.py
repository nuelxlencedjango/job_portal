# Generated by Django 3.2 on 2022-03-25 16:21

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artisan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.RenameField(
            model_name='artisan',
            old_name='date_created',
            new_name='date_joined',
        ),
        migrations.AddField(
            model_name='artisan',
            name='profile_img',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='artisan',
            name='phone',
            field=models.CharField(max_length=15, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='artisan',
            name='profession_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='artisan.profession'),
        ),
    ]
