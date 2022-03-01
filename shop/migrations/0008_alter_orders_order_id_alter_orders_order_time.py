# Generated by Django 4.0.2 on 2022-03-01 08:55

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_orders_customer_alter_orders_order_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order_id',
            field=models.CharField(default=uuid.UUID('41f82e0d-ca05-4e3b-826e-3440de8c6d5c'), max_length=256, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 1, 14, 25, 39, 380119)),
        ),
    ]
