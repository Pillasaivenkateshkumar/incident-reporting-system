from django.shortcuts import render
from .models import Incident

def index(request):

    incidents = Incident.objects.all()

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