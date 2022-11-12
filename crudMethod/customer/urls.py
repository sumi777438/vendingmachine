from django.urls import path
from .import views
urlpatterns = [
    path('', views.vendingMachine_func,name='vendingMachine'),
    path('vendingMachine/details/<str:machine_code>/', views.vendingMachine_Details,name='vendingMachine_Details'),
    path('checkout/<str:prod_id>/<str:vmCode>/', views.checkout_page,name='checkout_page'),
    path('invoice/<str:prod_id>/<str:vmCode>/', views.invoice_page,name='invoice_page'),

]
