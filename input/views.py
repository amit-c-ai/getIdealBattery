from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import batteryDetailForm
from .models import batteryDetail

# Create your views here.
def home(request):
    form = batteryDetailForm()
    if request.method == "POST":
        no_of_cells = request.POST.get('no_of_cells')
        voltage = request.POST.get('voltage')
        c_count = request.POST.get('c_count')
        mAh = request.POST.get('mAh')

        context = {'no_of_cells':no_of_cells, 'voltage':voltage, 'c_count':c_count, 'mAh':mAh}
        return render(request, 'input/resultpage.html', context)


    context = {'form':form}
    return render(request, 'input/homepage.html', context)

# def result(request):
#     context = {}
#     return render(request, 'input/resultpage.html', context)