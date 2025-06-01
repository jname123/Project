from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.
class Inquiry(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_inquiries') # 메시지 보낸 사람
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_inquiries') # 판매자
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='inquiries') # 어떤 상품에 대한 문의인지
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username} → {self.receiver.username}: {self.product.title}"