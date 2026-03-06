from django.shortcuts import render, redirect, get_object_or_404
from .models import Incident
from .forms import IncidentForm

# ----------------------------
# Dashboard / Home page
# ----------------------------
def index(request):
    incidents = Incident.objects.all()

    # Counters for dashboard
    total_incidents = incidents.count()
    new_incidents = incidents.filter(status="New").count()
    inprogress_incidents = incidents.filter(status="InProgress").count()
    resolved_incidents = incidents.filter(status="Resolved").count()

    context = {
        "incidents": incidents,
        "total_incidents": total_incidents,
        "new_incidents": new_incidents,
        "inprogress_incidents": inprogress_incidents,
        "resolved_incidents": resolved_incidents,
    }

    return render(request, "incidents/index.html", context)

# ----------------------------
# Create a new Incident
# ----------------------------
def create_incident(request):
    if request.method == "POST":
        form = IncidentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to dashboard
    else:
        form = IncidentForm()
    return render(request, "incidents/create.html", {"form": form})

# ----------------------------
# Update an existing Incident
# ----------------------------
def update_incident(request, pk):
    incident = get_object_or_404(Incident, pk=pk)
    if request.method == "POST":
        form = IncidentForm(request.POST, instance=incident)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = IncidentForm(instance=incident)
    return render(request, "incidents/update.html", {"form": form, "incident": incident})

# ----------------------------
# Delete an Incident
# ----------------------------
def delete_incident(request, pk):
    incident = get_object_or_404(Incident, pk=pk)
    if request.method == "POST":
        incident.delete()
        return redirect('index')
    return render(request, "incidents/delete.html", {"incident": incident})