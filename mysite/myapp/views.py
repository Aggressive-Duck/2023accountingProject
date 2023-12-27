from django.shortcuts import render, redirect
from .forms import LedgerIncomeModelForm, LedgerExpenseModelForm
from .models import LedgerIncome, LedgerExpense
from django.db.models import Sum


# Create your views here.
def dashboard(request):
    empty = {}

    # income
    income = LedgerIncome.objects.all()
    incomeForm = LedgerIncomeModelForm()

    # expense
    expense = LedgerExpense.objects.all()
    expenseForm = LedgerExpenseModelForm()

    incomeSum = LedgerIncome.objects.aggregate(Sum('receiptNumber'))

    context = {
        'incomeSum': incomeSum
    }

    return render(request, "myapp/dashboard.html", context)





def index(request):

    #income
    income = LedgerIncome.objects.all()
    incomeForm = LedgerIncomeModelForm()

    #expense
    expense = LedgerExpense.objects.all()
    expenseForm = LedgerExpenseModelForm()



    if request.method == 'POST':
        incomeForm = LedgerIncomeModelForm(request.POST)
        expenseForm = LedgerExpenseModelForm(request.POST)
        if incomeForm.is_valid():
            incomeForm.save()
        elif expenseForm.is_valid():
            expenseForm.save()
        return redirect('/')


    context = {
        'income' : income,
        'incomeForm': incomeForm,
        'expense' : expense,
        'expenseForm': expenseForm,
    }

    return render(request, 'myapp/index.html', context)


def updateIncome(request, pk):

    income = LedgerIncome.objects.get(id=pk)

    incomeForm = LedgerIncomeModelForm(instance=income)


    if request.method == 'POST':
        incomeForm = LedgerIncomeModelForm(request.POST, instance=income)
        if incomeForm.is_valid():
            incomeForm.save()
        return redirect('/')

    context = {
        'incomeForm': incomeForm,
    }

    return render(request, 'myapp/updateIncome.html', context)

def updateExpense(request, pk):

    expense = LedgerExpense.objects.get(id=pk)

    expenseForm = LedgerExpenseModelForm(instance=expense)


    if request.method == 'POST':
        expenseForm = LedgerExpenseModelForm(request.POST, instance=expense)
        if expenseForm.is_valid():
            expenseForm.save()
        return redirect('/')

    context = {
        'expenseForm': expenseForm,
    }

    return render(request, 'myapp/updateExpense.html', context)




def deleteIncome(request, pk):

    income = LedgerIncome.objects.get(id=pk)

    if request.method == 'POST':
        income.delete()
        return redirect('/')

    context = {
            'income': income
    }

    return render(request, 'myapp/deleteIncome.html', context)

def deleteExpense(request, pk):

    expense = LedgerExpense.objects.get(id=pk)

    if request.method == 'POST':
        expense.delete()
        return redirect('/')

    context = {
            'expense': expense
    }

    return render(request, 'myapp/deleteExpense.html', context)


#empty = {}
#return render(request, "myapp/index.html", empty)