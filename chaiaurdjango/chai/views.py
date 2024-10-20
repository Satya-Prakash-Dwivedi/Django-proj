from django.shortcuts import render, get_object_or_404
from .models import chaiVariety , Store
from .forms import chaiVariteyForm

# Create your views here.

def all_chai(request):
    chais = chaiVariety.objects.all()
    return render(request, 'chai/all_chai.html', {'chais' : chais})

def chai_detail(request, chai_id):
    chai = get_object_or_404(chaiVariety, pk=chai_id)
    return render(request, 'chai/chai_detail.html', {'chai' : chai})

def chai_store_view(request):
    stores = None
    if request.method == "POST":
        form = chaiVariteyForm(request.POST)
        if form.is_valid():
           chai_variety = form.cleaned_data('chaiVariety')
           stores = Store.objects.filter(chai_varieties = chai_variety)
    else:
        form = chaiVariteyForm()
    
    return render(request, 'chai/chai_stores.html', {'form' : form, 'stores': stores})
