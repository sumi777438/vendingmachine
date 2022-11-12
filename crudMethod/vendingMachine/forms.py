from django import forms
from vendingMachine.models import vendingMachine
class vendingMachineUpdateForm(forms.ModelForm):
    vendingMachine_id = forms.CharField(label ='Machine id', max_length=20)
    machine_code = forms.CharField(label ='Machine code', max_length=100)
    located_at = forms.CharField(label ='located', max_length=255)
    capacity = forms.IntegerField(label ='capacity')
    payment_method = forms.CharField(label ='payment method', max_length=100)

    class Meta:
        model =vendingMachine
        fields=['vendingMachine_id','machine_code','located_at','capacity','payment_method']

    def __init__(self,*args,**kwargs):
        super(vendingMachineUpdateForm,self).__init__(*args,**kwargs)
        self.fields['vendingMachine_id'].widget.attrs['class']='form-control'
        self.fields['machine_code'].widget.attrs['class'] = 'form-control'
        self.fields['located_at'].widget.attrs['class'] = 'form-control'
        self.fields['capacity'].widget.attrs['class'] = 'form-control'
        self.fields['payment_method'].widget.attrs['class'] = 'form-control'

