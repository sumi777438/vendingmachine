from django.contrib import admin

# Register your models here.
from .models import *
class vendingMachineAdmin(admin.ModelAdmin):
     list_display=['vendingMachine_id','machine_code','located_at','capacity','available_product_quantity','payment_method']
     list_display_links = ['vendingMachine_id']

class productAdmin(admin.ModelAdmin):
     list_display=['product_id','product_name','product_price']

class TransactionAdmin(admin.ModelAdmin):
     list_display=['transaction_id','vendingMachine','product','price','transaction_date']

admin.site.register(vendingMachine,vendingMachineAdmin)
admin.site.register(product,productAdmin)
admin.site.register(Transaction,TransactionAdmin)
