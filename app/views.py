from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm
from django.http import JsonResponse
from .models import Expense
import datetime
import json

# Create your views here.

def home(request):
    expenses = Expense.objects.all().order_by('-date')
    total_expense = sum(exp.amount for exp in expenses)

    return render(request, 'expense-tracker.html', {
        'expenses': expenses,
        'total_expense': total_expense
    })

def add_expense(request):
    if request.method == 'POST':
        name = request.POST['name']
        amount = request.POST['amount']
        category = request.POST['category']
        Expense.objects.create(name=name, amount=amount, category=category)
        return redirect('home')
    return redirect('home')

def delete_expense(request, id):
    Expense.objects.get(id=id).delete()
    return redirect('home')

def get_expense_data(request):
    today = datetime.date.today()
    monthly_expenses = Expense.objects.filter(date__year=today.year, date__month=today.month)
    yearly_expenses = Expense.objects.filter(date__year=today.year)

    daily_data = {}
    monthly_data = {}
    yearly_total = sum(exp.amount for exp in yearly_expenses)

    for exp in monthly_expenses:
        day = exp.date.day
        daily_data[day] = daily_data.get(day, 0) + exp.amount

    for exp in yearly_expenses:
        month = exp.date.strftime('%B')
        monthly_data[month] = monthly_data.get(month, 0) + exp.amount

    return JsonResponse({
        'daily': daily_data,
        'monthly': monthly_data,
        'yearly_total': yearly_total
    })

def landingpage(request):
  if request.user.is_authenticated:
        return redirect('about') 
  return render(request, 'landingpage.html')


def about(request):
  return render(request, 'about.html')

def tutorials(request):
  return render(request, 'tutorials.html')

def emiCalculator(request):
  return render(request, 'emi-calculator.html')

def expenseTracker(request):
  return render(request, 'expense-tracker.html')

def financialPlanning(request):
  return render(request, 'financial_planning.html')

def investmentPortfolio(request):
  return render(request, 'investment-portfolio.html')

def sipCalculator(request):
  return render(request, 'sip_calculator.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # Redirect to About Us page after registration
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('about')  # Redirect to About Us page after login
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

def about(request):
    return render(request, 'about.html')
