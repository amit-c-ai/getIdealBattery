from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import maxCurrentForm, chargeTimeForm, batteryChooseForm, continuousCurrForm, burstsCurrForm, dischargeTimeForm
# from .models import maxCurrent, chargeTime, batteryChoose

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
        idl_curr_2 = 2*idl_curr
        idl_curr_3 = 3*idl_curr
        context = {'idl_curr':idl_curr, 'idl_curr_2':idl_curr_2, 'idl_curr_3':idl_curr_3}
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
        capacity = (float(current)/c_rating)*1000
        context = {'c_rating':c_rating, 'capacity':capacity}
        return render(request, 'input/resultpagebatterychoose.html', context)

    context = {'form':form}
    return render(request, 'input/batterychoose.html', context)   

def contcurr(request):
    form = continuousCurrForm()
    if request.method == "POST":
        capacity = request.POST.get('capacity')
        cont_curr = request.POST.get('continuous_current')
        
        c_rating = (float(cont_curr)*1000)/capacity
        context = {'c_rating':c_rating}
        return render(request, 'input/resultpagecontcurr.html', context)

    context = {'form':form}
    return render(request, 'input/contcurr.html', context) 

def burstcurr(request):
    form = burstsCurrForm()
    if request.method == "POST":
        capacity = request.POST.get('capacity')
        c_rating = request.POST.get('c_rating')
        
        burst_curr = (int(capacity)*float(c_rating))/1000
        context = {'burst_curr':burst_curr}
        return render(request, 'input/resultpageburstcurr.html', context)

    context = {'form':form}
    return render(request, 'input/burstcurr.html', context) 

def dischargetime(request):
    form = dischargeTimeForm()
    if request.method == "POST":
        c_rating = request.POST.get('c_rating')
        
        dis_curr = 60/float(c_rating)
        context = {'dis_curr':dis_curr}
        return render(request, 'input/resultpagediscurr.html', context)

    context = {'form':form}
    return render(request, 'input/discurr.html', context) 