from django.urls import path
from .views import *

urlpatterns=[
  path('',landingpage,name='landingpage'),
  path('register/', register, name='register'),
  path('login/', user_login, name='login'),
  path('logout/', user_logout, name='logout'),
  path('about/', about, name='about'),
  path('tutorials/', tutorials, name='tutorials'),
  path('emiCalculator/', emiCalculator, name='emiCalculator'),
  path('expenseTracker/', expenseTracker, name='expenseTracker'),
  path('financialPlanning/', financialPlanning, name='financialPlanning'),
  path('investmentPortfolio/', investmentPortfolio, name='investmentPortfolio'),
  path('sipCalculator/', sipCalculator, name='sipCalculator'),
  path('home/', home, name='home'),
  path('add/', add_expense, name='add_expense'),
  path('delete/<int:id>/', delete_expense, name='delete_expense'),
  path('get_expense_data/', get_expense_data, name='get_expense_data'),
]