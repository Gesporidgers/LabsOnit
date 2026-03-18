from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, JsonResponse
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

def changestatus(request : HttpRequest, id : int):
    if request.method == 'PUT':
        flight = Flight.get_object_or_404(Flight, id=id)
        flight.completed = request.PUT.get('completed')
        flight.save()

        return JsonResponse{"status": "changed successfully"}

# Create your views here.
