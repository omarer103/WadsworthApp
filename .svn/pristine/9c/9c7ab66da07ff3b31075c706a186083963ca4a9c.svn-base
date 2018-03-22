from django.shortcuts import render
from .models import Transaction, BudgetAmount, BudgetCategory
from .forms import BudgetAmountForm, BudgetCategoryForm, CategoryDeleteForm
# Create your views here.


def index(request):
    '''
    View for getting the list of transactions on the home page / index.
    :param request:
    :return:
    '''
    transaction_list = Transaction.objects.all()
    return render(request, 'BankData/index.html',
                  {'transaction_list':transaction_list})


def budget(request):
    '''
    View for the budget page.
    :param request:
    :return:
    '''
    try:
        budget_max = BudgetAmount.objects.get()
    except BudgetAmount.DoesNotExist:
        budget_max = 0
    budget_category_list = BudgetCategory.objects.all()
    bcl_names = list(BudgetCategory.objects.values_list('name', flat=True))
    bcl_values = list(BudgetCategory.objects.values_list('amount', flat=True))

    if request.method == 'POST':
        if 'submit' in request.POST:
            if BudgetAmount.objects.exists():
                budget_max.delete()
            ba_form = BudgetAmountForm(request.POST)
            if ba_form.is_valid():
                ba = ba_form.save(commit=False)
                ba.save()
            bc_form = BudgetCategoryForm()
            dl_form = CategoryDeleteForm()

        elif 'add' in request.POST:
            bc_form = BudgetCategoryForm(request.POST)
            if bc_form.is_valid():
                bc = bc_form.save(commit=False)
                bc.save()
            ba_form = BudgetAmountForm()
            dl_form = CategoryDeleteForm()

        elif 'delete' in request.POST:
            dl_form = CategoryDeleteForm(request.POST)
            item_name = request.POST.get('name')
            item = BudgetCategory.objects.filter(name=item_name)
            item.delete()
            bc_form = BudgetCategoryForm()
            ba_form = BudgetAmountForm()

    else:
        bc_form = BudgetCategoryForm()
        ba_form = BudgetAmountForm()
        dl_form = CategoryDeleteForm()

    return render(request, 'BankData/budget.html',
                  {'budget_max': budget_max,
                   'budget_category_list': budget_category_list,
                   'bcl_names': bcl_names,
                   'bcl_values': bcl_values,
                   'ba_form': ba_form,
                   'bc_form': bc_form,
                   'dl_form': dl_form})


