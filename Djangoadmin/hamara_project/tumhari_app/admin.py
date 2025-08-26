from django.contrib import admin
from . import models

# Register your models here.
admin.site.site_header="Hamari App E-commerce"
admin.site.site_title="E-commerce"
admin.site.index_title="Dashboard"
admin.site.register(models.Brand)
admin.site.register(models.Category)
admin.site.register(models.Product)
admin.site.register(models.Contact)