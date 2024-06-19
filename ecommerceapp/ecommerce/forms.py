from django import forms
from ecommerce.models import UserProfile
from cart.models import Address

class UserForm(forms.ModelForm):
        class Meta:
            model=UserProfile
            fields='__all__'
class AddressForm(forms.ModelForm):
      class Meta:
            model=Address
            fields=['address','phone','zip_code','city','country']