from django.contrib import admin
from .models import *

admin.site.register(Categories)
admin.site.register(Tags)
admin.site.register(Products)
admin.site.register(Customers)
admin.site.register(Orders)

