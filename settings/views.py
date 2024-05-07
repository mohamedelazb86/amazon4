from django.shortcuts import render
from .models import Setting


def home(request):
    return render(request,"settings/home.html",{})
