from django.shortcuts import render
from .models import chai_variety,Store
from django.shortcuts import get_object_or_404
from .forms import Chai_Variety_form

def all_chai(request):
    chais = chai_variety.objects.all()
    return render(request, 'chai/all_chai.html', {'chais': chais})

def chai_detail(request, chai_id):
    chai = get_object_or_404(chai_variety, pk = chai_id)
    return render(request, 'chai/chai_detail.html',{'chai': chai})

def chai_store_view(request):
    stores = None
    if request.method == 'POST':
        form = Chai_Variety_form(request.POST)
        if form.is_valid():
            chai_variety = form.cleaned_data['chai_variety']
            stores = Store.objects.filter(chai_varity = chai_variety)
    
    return render(request, 'chai/chai_stores.html',{'stores':stores, 'form':form})