from django.contrib import admin

# Register your models here.
from .models import LedgerIncome
from .models import LedgerExpense

class LedgerIncomeAdmin(admin.ModelAdmin):
    list_display = ('receiptDescription', 'receiptType', 'receiptNumber', 'recieptDate')
    ordering = ('id',)
admin.site.register(LedgerIncome, LedgerIncomeAdmin)

class LedgerExpenseAdmin(admin.ModelAdmin):
    list_display = ('expenseDescription', 'expenseType', 'expenseNumber', 'expenseDate')
    ordering = ('id',)
admin.site.register(LedgerExpense, LedgerExpenseAdmin)
