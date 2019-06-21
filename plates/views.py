from datetime import timezone
from django.shortcuts import render, redirect
from .models import Plate
from .forms import PlateForm


def index(request):
    plates = Plate.objects.all()
    return render(request, 'index.html', {'plates': plates})


def new(request):
    if request.method == "POST":
        form = PlateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PlateForm()
    return render(request, 'edit.html', {'form': form})

def overview(request):
    return render(request, 'overview.html')