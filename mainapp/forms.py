from django import forms
from django.forms import ModelMultipleChoiceField, ModelChoiceField

from mainapp.models import FoodOptions, Order


class OrderForm(forms.ModelForm):
    bread = ModelChoiceField(queryset=FoodOptions.objects.filter(food_type_options__name='Bread'),
                             widget=forms.Select)
    vegetables = ModelMultipleChoiceField(queryset=FoodOptions.objects.filter(food_type_options__name='Vegetables'),
                                          widget=forms.CheckboxSelectMultiple)
    sauce = ModelMultipleChoiceField(queryset=FoodOptions.objects.filter(food_type_options__name='Sauce'),
                                     widget=forms.CheckboxSelectMultiple, label="Sauce")
    oven_baked = forms.BooleanField(required=False)
    size = forms.ChoiceField(choices=Order.SIZE_CHOICES, widget=forms.Select(), required=True)
    extra = forms.CharField(widget=forms.Textarea(), required=False)

    class Meta:
        model = Order
        fields = ['bread', 'vegetables', 'sauce', 'oven_baked', 'size', 'extra']