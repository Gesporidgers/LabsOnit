from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Flight


def index(request : HttpRequest):
    if request.method == 'POST':
        Flight.objects.create(
            origin = request.POST.get('origin'),
            origin_icao = request.POST.get('originICAO'),
            dest = request.POST.get('dest'),
            dest_icao = request.POST.get('destICAO')
        )
        return redirect('/')
    flights = Flight.objects.all()
    return render(request, 'index.html', {"flights":flights})

def changestatus(request):
    pass

# Create your views here.
