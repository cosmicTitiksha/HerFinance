from django.db import models

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Transport', 'Transport'),
        ('Entertainment', 'Entertainment'),
        ('Shopping', 'Shopping'),
        ('Bills', 'Bills'),
        ('Others', 'Others'),
    ]
    
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Others')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - ₹{self.amount}"

