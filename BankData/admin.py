from django.contrib import admin
from .models import Transaction, BudgetAmount, BudgetCategory

admin.site.register(Transaction)
admin.site.register(BudgetAmount)
admin.site.register(BudgetCategory)