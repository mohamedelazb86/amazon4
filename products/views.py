from django.shortcuts import render
from .models import Product,Brand,Review,ImagePOroduct
from django.views.generic import ListView,DetailView
from django.db.models.aggregates import Count


class Product_List(ListView):
    model=Product
    template_name='products/product_list.html'
    paginate_by=24

class Product_Detail(DetailView):
    model=Product
    template_name='products/product_detail.html'

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.filter(product=self.get_object())
        context["images"] = ImagePOroduct.objects.filter(product=self.get_object())
        context["related"] = Product.objects.filter(brand=self.get_object().brand)

        return context
    

class Brand_list(ListView):
    model=Brand
    template_name='products/brand_list.html'
    paginate_by=25
    queryset=Brand.objects.annotate(product_count=Count('product_brand'))

class Brand_Detail(DetailView):
    model=Brand
    template_name='products/brand_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related"] = Product.objects.filter(brand=self.get_object())
        return context
    
