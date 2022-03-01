# Generated by Django 4.0.2 on 2022-03-01 06:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_orders_order_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='customer',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='shop.customers'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 1, 11, 46, 23, 460501)),
        ),
    ]