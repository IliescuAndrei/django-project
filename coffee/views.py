from django.shortcuts import render
from coffee.models import Cafea
# Create your views here.

def cafea_index(request):
    cafele = Cafea.objects.all()
    context = {
        'cafele': cafele
    }
    return render(request, 'cafea_index.html', context)

def cafea_detail(request):
    cafea = Cafea.objects.get(pk=pk)
    context = {
        'cafea': cafea
    }
    return render(request, 'cafea_detail.html', context)

