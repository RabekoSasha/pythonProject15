from django import forms
from django.forms import ModelForm, TextInput, Textarea
from .models import Order, Review


class OrderForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['order_date'].label = 'Дата получения заказа'

    order_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = Order
        fields = (
            'first_name', 'last_name', 'phone', 'address', 'buying_type', 'order_date', 'comment'
        )


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["name", "message"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название',
            }),
            "message": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст',
            })
        }
