from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['image', 'title', 'category', 'price', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '제품명을 입력하세요'}),
            'price': forms.NumberInput(attrs={'placeholder': '가격을 입력하세요'}),
            'description': forms.Textarea(attrs={
                'placeholder': '제품 설명을 입력하세요',
                'rows': 6,      # 원하는 행 개수로 늘려주세요
                'cols': 40,     # 필요시 열 개수도 지정
                # 'style': 'resize: both;', # 크기 조절 핸들 나오게 하고 싶으면 추가
            }),
        }