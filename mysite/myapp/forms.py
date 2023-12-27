from django import forms
from .models import LedgerIncome, LedgerExpense

class LedgerIncomeModelForm(forms.ModelForm):
    class Meta:
        model = LedgerIncome
        fields = '__all__'
        widgets = {
            'receiptType': forms.Select(attrs={'class': 'custom-select'}),
            'receiptDescription' : forms.TextInput(attrs={'class' : 'form-control'}),
            'receiptNumber': forms.NumberInput(attrs={'class': 'form-control'}),
            'recieptDate': forms.DateInput(attrs={'class': 'form-control', 'type':"date" }),
        }
        labels = {
            'receiptType': '選擇分類',
            'receiptDescription': '明細描述',
            'receiptNumber': '明細價格',
            'recieptDate': '日期',
        }

class LedgerExpenseModelForm(forms.ModelForm):
    class Meta:
        model = LedgerExpense
        fields = '__all__'
        widgets = {
            'expenseType': forms.Select(attrs={'class': 'custom-select'}),
            'expenseDescription': forms.TextInput(attrs={'class': 'form-control', 'id': 'exampleFormControlInput1'}),
            'expenseNumber': forms.NumberInput(attrs={'class': 'form-control'}),
            'expenseDate': forms.DateInput(attrs={'class': 'form-control', 'type': "date"}),
        }
        labels = {
            'expenseType': '選擇分類',
            'expenseDescription': '明細描述',
            'expenseNumber': '明細價格',
            'expenseDate': '日期',
        }

