from django.urls import path

from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.index, name='index'),
    path('updateIncome/<str:pk>', views.updateIncome, name='UpdateIncome'),
    path('deleteIncome/<str:pk>', views.deleteIncome, name='DeleteIncome'),
    path('updateExpense/<str:pk>', views.updateExpense, name='UpdateExpense'),
    path('deleteExpense/<str:pk>', views.deleteExpense, name='DeleteExpense'),
]