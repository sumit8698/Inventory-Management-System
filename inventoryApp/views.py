from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Product, Order
from .forms import ProductForm, OrderForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='UserApp:user-login')
def index(request):
    product = Product.objects.all()
    product_count = product.count()
    order = Order.objects.all()
    order_count = order.count()
    customer = User.objects.filter(groups=2)
    customer_count = customer.count()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.customer = request.user
            obj.save()
            return redirect('inventoryApp:index')
    else:
        form = OrderForm()
    context = {
        'form': form,
        'order': order,
        'product': product,
        'product_count': product_count,
        'order_count': order_count,
        'customer_count': customer_count,
    }
    return render(request, 'dashboard/index.html', context)

@login_required(login_url='UserApp:user-login')
def order(request):
    order = Order.objects.all()
    context ={
        'order': order,
    }
    return render(request, 'dashboard/order.html',context)

@login_required(login_url='UserApp:user-login')
def products(request):
    product = Product.objects.all()
    product_count = product.count()
    customer = User.objects.filter(groups=2)
    customer_count = customer.count()
    order = Order.objects.all()
    order_count = order.count()
    product_quantity = Product.objects.filter(name='')
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
            return redirect('inventoryApp:products')
    else:
        form = ProductForm()
    context = {
        'product': product,
        'form': form,
        'customer_count': customer_count,
        'product_count': product_count,
        'order_count': order_count,
    }
    return render(request, 'dashboard/products.html', context)

@login_required(login_url='UserApp:user-login')
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('inventoryApp:products')
    context = {
        'item': item
    }
    return render(request, 'dashboard/products_delete.html', context)



@login_required(login_url='user-login')
def product_edit(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('inventoryApp:products')
        else:
            return render(request, 'dashboard/products_delete.html')
    else:
        form = ProductForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/products_edit.html', context)

