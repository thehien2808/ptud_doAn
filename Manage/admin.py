from django.contrib import admin
from .models import  Staff,Customer, Supplier, Product, StockIn,StockOut

admin.site.register(Staff)
admin.site.register(Customer)
admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(StockOut)
admin.site.register(StockIn)
