from django.db import models
from django.forms import ModelForm

# Create your models here.

# EXPENSEorINCOME_CHOICE = {
#     "1" : "income",
#     "2" : "expense",
# }

RECIEPT_TYPE_CHOICE = {
    "薪資" : "薪資",
    "薪資所得" : "薪資所得",
    "兼職" : "兼職",
    "獎金" : "獎金",
    "發票/彩券收入" : "發票/彩券收入",
    "租金" : "租金",
    "優惠回饋" : "優惠回饋",
    "股利" : "股利",
    "投資獲利" : "投資獲利",
    "保險" : "保險",
    "退休金" : "退休金",
    "提款" : "提款",
    "贈與" : "贈與",
    "還錢" : "還錢",
}

EXPENSE_TYPE_CHOICE = {
    "飲食": "飲食",
    "服飾": "服飾",
    "住家": "住家",
    "交通": "交通",
    "學習": "學習",
    "休閒娛樂": "休閒娛樂",
    "購物": "購物",
    "醫療": "醫療",
    "現金消費": "現金消費",
    "保險": "保險",
    "費用/手續費": "費用/手續費",
    "稅金": "稅金",
    "繳費": "繳費",
    "娛樂": "娛樂",
}

class LedgerIncome(models.Model):
    #expenseOrIncome = models.CharField(max_length=100, choices=EXPENSEorINCOME_CHOICE, null=False)
    receiptDescription = models.CharField(max_length=100, null=False)
    receiptType = models.CharField(max_length=255, choices=RECIEPT_TYPE_CHOICE)
    receiptNumber = models.IntegerField()
    recieptDate = models.DateField()


class LedgerExpense(models.Model):
    expenseDescription = models.CharField(max_length=100, null=False)
    expenseType = models.CharField(max_length=255, choices=EXPENSE_TYPE_CHOICE)
    expenseNumber = models.IntegerField()
    expenseDate = models.DateField()

