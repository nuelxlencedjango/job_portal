# Generated by Django 3.2 on 2022-04-20 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artisan', '0013_completedjob'),
        ('products', '0006_alter_orderitem_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='artisan_assigned',
            field=models.ManyToManyField(blank=True, to='artisan.Artisan'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='date_created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]