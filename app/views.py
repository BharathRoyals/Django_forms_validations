from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse

def cricket(request):
    CFO=CricketForm()
    d={'CFO':CFO}
    if request.method=='POST':
        FD=CricketForm(request.POST)
        if FD.is_valid():
            return HttpResponse(str(FD.cleaned_data))
    return render(request,'cricket.html',d)