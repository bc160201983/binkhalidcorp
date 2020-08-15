from django.shortcuts import render
from .models import Category, Stock
from .forms import RawCategoryForm
# Create your views here.

def category_view(request):

    my_form = RawCategoryForm()
    if request.method == "POST":
        my_form = RawCategoryForm(request.POST)
        if my_form.is_valid():
            print(my_form.changed_data)
            Category.objects.create(**my_form.cleaned_data)
            my_form = RawCategoryForm()
    category = Category.objects.all()

    context= {
        "form":my_form,
        "cat": category
    }

    return render(request, 'category.html', context)

def stock_view(request):

    stock = Stock.objects.all()
    context = {
        "stock": stock
    }

    return render(request, 'stock/index.html', context)

def stock_create(request):

    context = {

    }

    return render(request, 'stock/create.html', context)