from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category
from .forms import ProductForm
from django.contrib.auth.decorators import login_required


@login_required
def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user  # 판매자 지정
            product.save()
            return redirect('products_list')  # 메인 페이지로 이동
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form': form})

@login_required
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk, seller=request.user)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/product_form.html', {'form': form})

@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk, seller=request.user)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'products/product_confirm_delete.html', {'product': product})

def product_list(request):
    query = request.GET.get('q')
    selected_category = request.GET.get('category')
    products = Product.objects.all()
    categories = Category.objects.all()

    if query:
        products = products.filter(title__icontains=query)

    if selected_category:
        products = products.filter(category__id=selected_category)

    products = Product.objects.all()

    return render(request, 'products/product_list.html', {
        'products': products,
        'query': query,
        'categories': categories,
        'selected_category': selected_category,
    })

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})

def category_view(request, category_name):
    products = Product.objects.filter(category__name=category_name)
    context = {'products': products, 'category_name': category_name}
    return render(request, 'category/category_page.html', context)

