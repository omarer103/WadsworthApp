from django.test import TestCase
from .models import Transaction
from .forms import BudgetAmountForm, BudgetCategoryForm

# Tests transaction model
class TransactionTestCase(TestCase):
    def test_transactions(self):
        '''
        Creates a test transaction and makes sure all
        the parameters are correctly set.
        :return:
        '''
        Transaction.objects.create(details="DEBIT", postingDate="11/4/2016",
                                   description="Test Description", amount=-50,
                                   type="DEBIT_CARD", balance=500,
                                   checkOrSlipNum="")
        test_transaction = Transaction.objects.get(description="Test Description")
        self.assertEquals(test_transaction.details, "DEBIT")
        self.assertEquals(test_transaction.postingDate, "11/4/2016")
        self.assertEquals(test_transaction.amount, -50)
        self.assertEquals(test_transaction.type, "DEBIT_CARD")
        self.assertEquals(test_transaction.balance, 500)
        self.assertEquals(test_transaction.checkOrSlipNum, "")

class BudgetForms(TestCase):
    def test_budget(self):
        form_data = {'amount': 3000}
        form = BudgetAmountForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_budget_negative(self):
        form_data = {'amount': -1000}
        form = BudgetAmountForm(data=form_data)
        self.assertTrue(form.is_valid())


class CategoryForms(TestCase):
    def test_category(self):
        form_data = {'name': 'Candy', 'amount': 500}
        form = BudgetCategoryForm(data=form_data)
        self.assertTrue(form.is_valid())


    def test_category_2(self):
        form_data = {'name': 'Food', 'amount': 'test'}
        form = BudgetCategoryFormForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_category_3(self):
        form_data = {'name': 100, 'amount': 'test'}
        form = BudgetCategoryForm(data=form_data)
        self.assertFalse(form.is_valid())