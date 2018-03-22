from django import forms
from models import BudgetCategory, BudgetAmount


class BudgetAmountForm(forms.ModelForm):
    class Meta:
        model = BudgetAmount
        fields = ('amount',)


class BudgetCategoryForm(forms.ModelForm):
    class Meta:
        model = BudgetCategory
        fields = ('name', 'amount',)


class CategoryDeleteForm(forms.ModelForm):
    class Meta:
        model = BudgetCategory
        fields = ('name',)