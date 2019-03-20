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
            plate = form.save(commit=False)
            # Plate.objects.last().counter + 1
            # plate.counter += int(1)
            plate.save()
            return redirect('root')
    else:
        form = PlateForm()
    return render(request, 'edit.html', {'form': form})

# import plate models for usage in shell
# from plates.models import Plate
