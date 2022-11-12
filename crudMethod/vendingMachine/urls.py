from django.urls import path
from .import views
urlpatterns = [
    path('vending-machine-list/', views.vending_list,name='vending_list'),
    path('vending-machine-remove/<str:machine_code>/', views.vendingDelete,name='vendingDelete'),
    path('vending-machine-update/<str:machine_code>/', views.vendingMachineUpdate, name='vendingMachineUpdate'),
    path('vending-machine-create/', views.vendingCreateFrom, name='vendingCreateFrom'),

    # crudproduct
    path('vending-machine-product-list/', views.vendingProductlist, name='vendingProductlist'),
    path('vending-machine-product-create/', views.createproduct, name='createproduct'),
    path('vending-machine-product-delete/<str:prod_id>/', views.productDelete, name='productDelete'),
    path('vending-machine-product-update/<str:prod_id>/', views.productUpdate, name='productUpdate'),

]
