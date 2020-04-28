# Generated by Django 3.0.3 on 2020-02-10 01:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shipping_addresses', '0002_auto_20200207_2300'),
        ('orders', '0002_order_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipping_address',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='shipping_addresses.ShippingAddress'),
            preserve_default=False,
        ),
    ]