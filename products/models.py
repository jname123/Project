from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(decimal_places=0, max_digits=10)  # 이거만 남기기
    created_at = models.DateTimeField(auto_now_add=True) # 상품 등록 시간
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=7)  # ← 방금 확인한 ID
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.title

