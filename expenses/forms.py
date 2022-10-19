from django import forms
from .models import Expense


class ExpenseSearchForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('name','date','category')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['date'].required = False
        self.fields['category'].required = False

    def date_search(self, *args, **kwargs):
        pass
