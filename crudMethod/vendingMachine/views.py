import random
import string

from django.shortcuts import render,redirect
from .models import *
from .forms import vendingMachineUpdateForm
# Create your views here.


def vending_list(request):
    result=vendingMachine.objects.all()
    context={
        'result':result,
    }
    return render(request, 'vendingMachine/vendingMachineCRUD/vending_list.html',context)

def vendingCreateFrom(request):

    result=vendingMachine.objects.all()
    if request.POST:
        # print('vendingMachine_id', request.POST['vendingMachine_id'])
        # print('machine_code', request.POST['machine_code'])
        # print('located_at', request.POST['located_at'])
        # print('capacity', request.POST['capacity'])
        # print('payment_method', request.POST['payment_method'])
        vendingMachine.objects.create(
            vendingMachine_id= request.POST['vendingMachine_id'],
            machine_code=request.POST['machine_code'],
            located_at=request.POST['located_at'],
            capacity=request.POST['capacity'],
            payment_method=request.POST['payment_method'],
        )

        return redirect('vending_list')

    context={
        'result':result
    }

    return render(request,'vendingMachine/vendingMachineCRUD/createFrom.html',context)
def vendingMachineUpdate(request,machine_code):
    # print("machine code",machine_code)
    vm_record=vendingMachine.objects.get(machine_code=machine_code)
    forms=vendingMachineUpdateForm(instance=vm_record)
    if request.POST:
        form = vendingMachineUpdateForm(request.POST, instance=vm_record)
        if form.is_valid():
            form.save()
            return redirect('vending_list')
        else:
            print('form is invalid!')
            print(form.errors.as_data())
    context={
        'forms':forms
    }
    return render(request,'vendingMachine/vendingMachineCRUD/vendingMachineUpdate.html',context)

def vendingDelete(request,machine_code):
    result=vendingMachine.objects.get(machine_code=machine_code)
    result.delete()
    return redirect('vending_list')


########product crud
def vendingProductlist(request):
    products =product.objects.all()
    # print(products)
    context={
        'products':products
    }

    return render(request,'vendingMachine/productCRUD/productList.html',context)

def productUpdate(request,prod_id):
    products=product.objects.get(product_id=prod_id)
    prod_vMachine=products.vendingMachine.all()
    vendMachine=vendingMachine.objects.all()

    if request.POST:
        # print('product id',request.POST['product_id'])
        # print('product name', request.POST['product_name'])
        # print('product price', request.POST['product_price'])
        # print('vendingMachine', request.POST.getlist('vendingMachine'))

        products.product_id = request.POST['product_id']
        products.product_name = request.POST['product_name']
        products.product_price = request.POST['product_price']

        for vm_remove in prod_vMachine:
            products.vendingMachine.remove(vm_remove.id)
        result=[vendingMachine.objects.get(machine_code=vm) for vm in request.POST.getlist('vendingMachine') ]
        print(result)

        for r in result:
            products.vendingMachine.add(r.id)

        products.save()


        return redirect('vendingProductlist')

    context={
       'products':products,
       'prod_vMachine':prod_vMachine,
       'vendMachine':vendMachine,
    }
    return render(request,'vendingMachine/productCRUD/productUpdate.html',context)


def productDelete(request,prod_id):
    prod=product.objects.get(product_id=prod_id)
    prod.delete()
    return redirect('vendingProductlist')
def createproduct(request):
    vendMachine = vendingMachine.objects.all()

    if request.POST:
        # print("product_id",request.POST['product_id'])
        # print("product_name", request.POST['product_name'])
        # print("product_price", request.POST['product_price'])
        # print("vendingMachine", request.POST.getlist('vendingMachine'))
        result = [vendingMachine.objects.get(machine_code=vm) for vm in request.POST.getlist('vendingMachine')]
        create_product= product.objects.create(
            product_id= request.POST['product_id'],
            product_name= request.POST['product_name'],
            product_price = request.POST['product_price'],

        )
        for vm in result:
            create_product.vendingMachine.add(vm.id)
        return redirect('vendingProductlist')


    context={
        'vendMachine':vendMachine
    }

    return render(request,'vendingMachine/productCRUD/productcretae.html',context)