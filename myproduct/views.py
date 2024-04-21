from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from .models import *
from .form import *
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import get_object_or_404


@login_required(login_url='user-login')
def farmer_board(request):
    return render(request, 'farmer/dashboard.html')


@login_required(login_url='user-login')
def add_product(request):
    if request.method == 'POST':
        form = products_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_success')  
    else:
        form = products_form()
    return render(request, 'product/add_product.html', {'form': form})

def success_add(request):
    return render(request, 'product/add_success.html')

@login_required(login_url='user-login')
def product_list(request):
    query = request.GET.get('search')
    if query:
        products = product.objects.filter(
            Q(name__icontains=query) |
            Q(origin__icontains=query) |
            Q(category__icontains=query) |
            Q(packaging__icontains=query) |
            Q(harvest_date__icontains=query) |
            Q(cost_price__icontains=query) |
            Q(Shelf_life__icontains=query) |
            Q(date_added__icontains=query)
        )
    else:
        products = product.objects.all()

    return render(request, 'product/product_list.html', {'products': products})

@login_required(login_url='user-login')
def product_edit(request):
    query = request.GET.get('search')
    if query:
        products = product.objects.filter(
            Q(name__icontains=query) |
            Q(origin__icontains=query) |
            Q(category__icontains=query) |
            Q(packaging__icontains=query) |
            Q(harvest_date__icontains=query) |
            Q(cost_price__icontains=query) |
            Q(Shelf_life__icontains=query) |
            Q(date_added__icontains=query)
        )
    else:
        products = product.objects.all()

    return render(request, 'product/product_edit.html', {'products': products})

def product_delete(request, pk):
    item_instance = get_object_or_404(product, id=pk)
    if request.method == 'POST':
        item_instance.delete()
        return redirect('add_success')
    return render(request, 'product/product_delete.html')

def product_update(request, pk):
    item = product.objects.get(id=pk)
    if request.method=='POST':
        form = products_form(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('add_success')
    else:
        form = products_form(instance=item)

    context={
        'form': form,
    }
    return render(request, 'product/product_update.html', context)

@login_required(login_url='user-login')
def sell_list(request):
    query = request.GET.get('search')
    if query:
        Sell_poultrys = Sell_poultry.objects.filter(
            Q(product__name__icontains=query) |
            Q(caption__icontains=query) 
        )
    else:
        Sell_poultrys = Sell_poultry.objects.all()  
        Sell_cerealss = Sell_cereals.objects.all()
        Sell_roottuberss = Sell_roottubers.objects.all()
        Sell_legumess = Sell_legumes.objects.all()
        Sell_cattles = Sell_cattle.objects.all()


        context = {
            'Sell_poultrys': Sell_poultrys,
            'Sell_cattles': Sell_cattles,
            'Sell_roottuberss': Sell_roottuberss,
            'Sell_legumess': Sell_legumess,
            'Sell_legumess': Sell_legumess,
            'Sell_cerealss': Sell_cerealss,
        }
    return render(request, 'product/sell_list.html', context)

def add_sell(request):
    if request.method == 'POST':
        form = Sell_poultry_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('sell_list')  
    else:
        form = Sell_poultry_form()
    return render(request, 'product/add_sell.html', {'form': form})

def add_sell_cattle(request):
    if request.method == 'POST':
        form = Sell_cattle_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('sell_list')  
    else:
        form = Sell_cattle_form()
    return render(request, 'product/add_sell_cattle.html', {'form': form})

def add_sell_legumes(request):
    if request.method == 'POST':
        form = Sell_legumes_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('sell_list')  
    else:
        form = Sell_legumes_form()
    return render(request, 'product/add_sell_legumes.html', {'form': form})

def add_sell_roottubers(request):
    if request.method == 'POST':
        form = Sell_roottubers_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('sell_list')  
    else:
        form = Sell_roottubers_form()
    return render(request, 'product/add_sell_roottubers.html', {'form': form})

def add_sell_cereals(request):
    if request.method == 'POST':
        form = Sell_cereals_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('sell_list')  
    else:
        form = Sell_cereals_form()
    return render(request, 'product/add_sell_cereals.html', {'form': form})

def Sell_poultry_delete(request, pk):
    item_instance = get_object_or_404(Sell_poultry, id=pk)
    if request.method == 'POST':
        item_instance.delete()
        return redirect('sell_list')
    return render(request, 'product/Sell_poultry_delete.html')

@login_required(login_url='user-login')
def sell_update(request):
    Sell_poultrys = Sell_poultry.objects.all()  
    Sell_cerealss = Sell_cereals.objects.all()
    Sell_roottuberss = Sell_roottubers.objects.all()
    Sell_legumess = Sell_legumes.objects.all()
    Sell_cattles = Sell_cattle.objects.all()


    context = {
        'Sell_poultrys': Sell_poultrys,
        'Sell_cattles': Sell_cattles,
        'Sell_roottuberss': Sell_roottuberss,
        'Sell_legumess': Sell_legumess,
        'Sell_legumess': Sell_legumess,
        'Sell_cerealss': Sell_cerealss,
        }

    return render(request, 'product/sell_update.html', context)

def Sell_cereals_delete(request, pk):
    item_instance = get_object_or_404(Sell_cereals, id=pk)
    if request.method == 'POST':
        item_instance.delete()
        return redirect('sell_list')
    return render(request, 'product/Sell_cereals_delete.html')

def Sell_roottubers_delete(request, pk):
    item_instance = get_object_or_404(Sell_roottubers, id=pk)
    if request.method == 'POST':
        item_instance.delete()
        return redirect('sell_list')
    return render(request, 'product/Sell_roottubers_delete.html')

def Sell_legumes_delete(request, pk):
    item_instance = get_object_or_404(Sell_legumes, id=pk)
    if request.method == 'POST':
        item_instance.delete()
        return redirect('sell_list')
    return render(request, 'product/Sell_legumes_delete.html')

def Sell_cattle_delete(request, pk):
    item_instance = get_object_or_404(Sell_cattle, id=pk)
    if request.method == 'POST':
        item_instance.delete()
        return redirect('sell_list')
    return render(request, 'product/Sell_cattle_delete.html')






@login_required(login_url='user-login')
def sell_dash(request):

    return render(request, 'farmer/sell.html')

def landing(request):
    poultrys = Sell_poultry.objects.all()
    cattles = Sell_cattle.objects.all()
    legumess = Sell_legumes.objects.all()
    roottuberss = Sell_roottubers.objects.all()
    cerealss = Sell_cereals.objects.all()

    context = {
        'poultrys': poultrys,
        'cattles': cattles,
        'legumess': legumess,
        'roottuberss': roottuberss,
        'cerealss': cerealss,
    }
    return render(request, 'product/landing.html', context)


@login_required
def add_to_cart(request, product, price):
    if request.user.is_authenticated:
        if 'cart' not in request.session:
            request.session['cart'] = []
        cart_item = {'product': product, 'price': price}
        request.session['cart'].append(cart_item)
        request.session.modified = True
        return redirect('landing')
    else:
        messages.info(request, 'Please log in to add items to your cart.')
        return redirect('user-login')

def cart_view(request):
    cart = request.session.get('cart', [])
    context = {'cart': cart}
    return render(request, 'product/cart.html', context)

def view_orders(request):
    cart = request.session.get('cart', [])
    context = {'cart': cart}
    return render(request, 'farmer/orders.html', context)
    

def remove_from_cart(request, product):
    if 'cart' in request.session:
        cart = request.session['cart']
        for item in cart:
            if item['product'] == product:
                cart.remove(item)
                request.session.modified = True
                break  
    return redirect('cart_view') 








@login_required(login_url='user-login')
def staff(request):
    workers = User.objects.all()
    context = {
        'workers': workers,
    }
    return render (request, 'dashboard/staff.html', context)

@login_required(login_url='user-login')
def products(request):
    items = product.objects.all()

    if request.method =="POST":
        form = products_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-products')
    else:
        form = products_form()
    
    context = {
        'items': items,
        'form': form,
    }

    return render (request, 'dashboard/products.html', context)

@login_required(login_url='user-login')
def order(request):
    orders = order.objects.all()

    context = {
        'orders': orders,
    }
    return render (request, 'dashboard/order.html', context)


def login(request):

    return render (request, 'user/login.html')





def staff_detail(request, pk):
    workers = User.objects.get(id=pk)
    context = {
        'worker': workers,
    }

    return render(request, 'dashboard/staff_detail.html', context)

