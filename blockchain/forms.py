from django.forms import ModelForm
from .models import Transaction
from web3 import Web3
#from betterforms.multiform import MultiModelForm


class ProducerForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['product_id','common_name','expiry_date','country','quantity','company','executor']        

class ShipperForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['product_id','common_name','country','quantity','company','executor']

class WholesalerForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['product_id','common_name','country','quantity','company','executor']
   
class DetailerForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['product_id','common_name','country','quantity','company']

# class LinksMultiForm(MultiModelForm):
#     form_classes = {
#         'producer': ProducerForm,
#         'shipper': ShipperForm,
#         'wholesaler': WholesalerForm,
#         'detailer': DetailerForm,
#     }
    



