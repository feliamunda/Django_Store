# Generated by Django 3.0.3 on 2020-02-08 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping_addresses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='line2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]