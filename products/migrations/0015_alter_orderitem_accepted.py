# Generated by Django 3.2 on 2022-04-26 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20220426_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='accepted',
            field=models.CharField(blank=True, default='No', max_length=100, null=True),
        ),
    ]
