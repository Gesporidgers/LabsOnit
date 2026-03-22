from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, JsonResponse
from .models import Flight
import json

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
        data = json.loads(request.body)
        flight = get_object_or_404(Flight, id=id)
        flight.completed = data.get('completed')
        flight.save()

        return JsonResponse({"status": "changed successfully"})

def changecell(request : HttpRequest, id : int):
    if request.method == 'PUT':
        data = json.loads(request.body)
        flight = get_object_or_404(Flight, id=id)
        setattr(flight,data.get('field'),data.get('value'))
        flight.save()

        return JsonResponse({"status": "changed successfully", "value": data.get('value')})

# Create your views here.
