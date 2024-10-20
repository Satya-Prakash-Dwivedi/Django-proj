from django.shortcuts import render, get_object_or_404
from .models import chaiVariety

# Create your views here.

def all_chai(request):
    chais = chaiVariety.objects.all()
    return render(request, 'chai/all_chai.html', {'chais' : chais})

def chai_detail(request, chai_id):
    chai = get_object_or_404(chaiVariety, pk=chai_id)
    return render(request, 'chai/chai_detail.html', {'chai' : chai})
