# Generated by Django 4.0.2 on 2022-03-01 08:53

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_remove_orders_customer_alter_orders_order_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.customers'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 1, 14, 23, 35, 224964)),
        ),
    ]
