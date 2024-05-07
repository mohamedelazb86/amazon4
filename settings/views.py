from django.shortcuts import render
from .models import Setting
from products.models import Brand,Product,Review
from django.db.models.aggregates import Count


def home(request):
    brands=Brand.objects.all()[:10].annotate(product_count=Count('product_brand'))
    sale_product=Product.objects.filter(flag='Sale')[:10]
    feature_product=Product.objects.filter(flag='Feature')[:6]
    new_product=Product.objects.filter(flag='New')
    reviews=Review.objects.all()[:10]


    context={
        'brands':brands,
        'sale_product':sale_product,
        'feature_product':feature_product,
        'new_product':new_product,
        'reviews':reviews
    }
    
    return render(request,"settings/home.html",context)
