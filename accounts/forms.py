from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer, Order, Product, StockItem

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'weight', 'category', 'description', 'tag', 'img']


class StockItemForm(ModelForm):
    class Meta:
        model = StockItem
        fields = ['name', 'weight', 'quantity']

        