import datetime

from django.contrib.auth.models import User
from django.db import models


class Categories(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_title = models.CharField(max_length=50)

    def __str__(self):
        return self.cat_title


class Tags(models.Model):
    tag_id = models.AutoField(primary_key=True)
    tag_title = models.CharField(max_length=20)

    def __str__(self):
        return self.tag_title


class Products(models.Model):
    p_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    qnt = models.IntegerField(default=1)
    rate = models.FloatField(default=0)
    cats = models.ManyToManyField(Categories)
    tags = models.ManyToManyField(Tags)

    def __str__(self):
        return self.name


class Customers(models.Model):
    customer_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)

    def __str__(self):
        return self.customer_name


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    products = models.ManyToManyField(Products)
    order_time = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return str(self.order_id)+" "+str(self.order_time)





