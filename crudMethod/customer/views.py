from django.shortcuts import render
from vendingMachine.models import *

# Create your views here.
def vendingMachine_func(request):
    vendingMachine_query = vendingMachine.objects.all()
    context={
        'vendMachine':vendingMachine_query,
      }
    return render(request,'customer/vendingMachine.html',context)
def vendingMachine_Details(request,machine_code):
    # print("machine code:",machine_code)
    vendingMacahine_record=vendingMachine.objects.get(machine_code=machine_code)
    products= product.objects.filter(vendingMachine =vendingMacahine_record)
    # print(products)
    context={
        'vendingMacahine_record':vendingMacahine_record,
        'products':products
    }
    return render(request,'customer/vendingMachineDetails.html',context)
def checkout_page(request,prod_id,vmCode):
    prod=product.objects.get(product_id=prod_id)
    # print('vending machine code:',vmCode)
    context={
        'prod':prod,
        'vmCode':vmCode,
    }
    return render(request,'customer/checkout.html',context)

# print out an invoice slip to the customer
def invoice_page(request,prod_id,vmCode):
    # print('product id:',prod_id)
    # print('vm code:',vmCode)
    prod = product.objects.get(product_id=prod_id)
    Vmachine=vendingMachine.objects.get(machine_code=vmCode)
    transcation = Transaction.objects.create(
        vendingMachine=Vmachine,
        product= prod,
        price = prod.product_price,
    )
    Vmachine.available_product_quantity -= 1
    Vmachine.save()

    context={
        'prod':prod,
        'Vmachine': Vmachine,
        'transcation': transcation,
    }

    return render(request,'customer/invoice.html',context)