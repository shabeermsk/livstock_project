from django import forms

from .models import Stock,Location,Unit
from seller.models import User

class StockForm(forms.ModelForm):
    location = forms.ModelMultipleChoiceField(queryset=Location.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)

    class Meta:

        exclude= {'user','slug','posted_date'}
        model = Stock

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
