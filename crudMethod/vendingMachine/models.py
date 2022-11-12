from django.db import models
import random,string

# Create your models here.
def random_string_generator(size=5,chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class vendingMachine(models.Model):
    vendingMachine_id = models.CharField(max_length=20)
    machine_code = models.CharField(max_length=100)
    located_at = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField(null=True,blank=True)
    available_product_quantity= models.PositiveIntegerField(null=True,blank=True)
    payment_method = models.CharField(max_length=100)
    vendMachine_image=models.ImageField( upload_to='vendMachineimage/',default='crudMethod/static/image/vending_machine.png',blank=True,null=True)

    def __str__(self):
        return self.machine_code

class product(models.Model):
    product_id = models.CharField(max_length=20)
    product_name = models.CharField(max_length=200)
    product_price = models.FloatField()
    vendingMachine = models.ManyToManyField(vendingMachine)
    product_image=models.ImageField(upload_to='productImage/', default='productImage/sample_product_image.png',blank=True,null=True)


    def __str__(self):
        return self.product_name


class Transaction(models.Model):
    transaction_id = models.CharField(max_length=20)
    vendingMachine = models.ForeignKey(vendingMachine,on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    transaction_date = models.DateTimeField(auto_now_add=True)

    def save(self,*args,**kwargs):
        pro=product.objects.get(id=self.product.id)
        self.price = pro.product_price
        if not len(self.transaction_id):
            self.transaction_id= self.vendingMachine.vendingMachine_id+'-'+self.product.product_name + '-'+ random_string_generator(size=50)
        super(Transaction,self).save(*args,**kwargs)
