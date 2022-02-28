# Generated by Django 4.0.2 on 2022-02-28 06:19

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('cat_id', models.AutoField(primary_key=True, serialize=False)),
                ('cat_title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('tag_id', models.AutoField(primary_key=True, serialize=False)),
                ('tag_title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('qnt', models.IntegerField(default=1)),
                ('rate', models.FloatField(default=0)),
                ('cats', models.ManyToManyField(to='shop.Categories')),
                ('tags', models.ManyToManyField(to='shop.Tags')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_time', models.DateTimeField(default=datetime.datetime(2022, 2, 28, 11, 49, 2, 416589))),
                ('products', models.ManyToManyField(to='shop.Products')),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=100)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
