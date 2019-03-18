from django.shortcuts import render
from django.http import HttpResponse
from .models import Plate

def index(request):
    plates = Plate.objects.all()
    return render(request, 'index.html', {'plates': plates})

def new(requst):
    return HttpResponse('New Plate')