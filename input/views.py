from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import maxCurrentForm, chargeTimeForm, batteryChooseForm
from .models import maxCurrent, chargeTime, batteryChoose

# Create your views here.
def home(request):
    return render(request, 'input/homepage.html')

def maxcurrent(request):
    form = maxCurrentForm()
    if request.method == "POST":
        capacity = request.POST.get('capacity')
        c_rating = request.POST.get('c_rating')
        max_curr = (int(capacity) * int(c_rating))/1000
        context = {'max_curr':max_curr}
        return render(request, 'input/resultpagemaxcurr.html', context)

    context = {'form':form}
    return render(request, 'input/maxcurrent.html', context)

def chargetime(request):
    form = chargeTimeForm()
    if request.method == "POST":
        capacity = request.POST.get('capacity')
        idl_curr = int(capacity)/1000
        context = {'idl_curr':idl_curr}
        return render(request, 'input/resultpagechargetime.html', context)

    context = {'form':form}
    return render(request, 'input/chargetime.html', context)

def batterychoose(request):
    form = batteryChooseForm()
    if request.method == "POST":
        voltage = request.POST.get('voltage')
        current = request.POST.get('current')
        run_time = request.POST.get('run_time')
        
        c_rating = 60/int(run_time)
        capacity = float(current)/c_rating
        context = {'c_rating':c_rating, 'capacity':capacity}
        return render(request, 'input/resultpagebatterychoose.html', context)

    context = {'form':form}
    return render(request, 'input/batterychoose.html', context)   