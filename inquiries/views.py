from django.shortcuts import render, redirect, get_object_or_404
from .models import Inquiry
from products.models import Product
from django.contrib.auth.decorators import login_required

# Create your views here.
def send_inquiry(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        message = request.POST.get('message')
        Inquiry.objects.create(
            sender=request.user,
            receiver=product.seller,
            product=product,
            message=message
        )
        return redirect('product_detail', pk=product_id)

    return render(request, 'inquiries/my_inquiries.html', {'product': product})

def send_inquiry(request, product_id):
    # ... 기존 구현 ...
    pass
def my_inquiries(request):
    # 예시: 본인의 문의 목록을 보여주는 뷰
    return render(request, 'inquiries/my_inquiries.html')

