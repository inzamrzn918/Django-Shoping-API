# Generated by Django 4.0.2 on 2022-03-01 06:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_orders_customer_alter_orders_order_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 1, 11, 47, 12, 771277)),
        ),
    ]
