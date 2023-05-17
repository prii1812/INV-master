from django import forms
from django.core.exceptions import ValidationError
from .models import Product,Issued_Items
class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['name','category','quantity','model','price']
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')

        if Product.objects.filter(name=name).exclude(id=self.instance.id).exists():
            raise ValidationError('Product already exists.')

        return cleaned_data

class orderform(forms.ModelForm):
    class Meta:
        model=Issued_Items
        fields=['product','issueditem_quantity','location']

class sendemailform(forms.Form):
    title=forms.CharField(label='Title',max_length=250 )
    empemail=forms.EmailField(label='Email id of employee')
    message=forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":25}))