# Generated by Django 3.2 on 2022-06-08 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_orderitem_work_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='artisanName',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]