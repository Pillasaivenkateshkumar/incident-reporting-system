from django.shortcuts import render, redirect, get_object_or_404
from .models import Incident
from .forms import IncidentForm

# READ
def index(request):
    incidents = Incident.objects.all()
    return render(request, 'incidents/index.html', {'incidents': incidents})

# CREATE
def create_incident(request):
    form = IncidentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'incidents/create.html', {'form': form})

# UPDATE
def update_incident(request, pk):
    incident = get_object_or_404(Incident, pk=pk)
    form = IncidentForm(request.POST or None, instance=incident)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'incidents/update.html', {'form': form})

# DELETE
def delete_incident(request, pk):
    incident = get_object_or_404(Incident, pk=pk)
    incident.delete()
    return redirect('index')