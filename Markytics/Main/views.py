from django.shortcuts import render,redirect
from .models import Forms
from django.http import HttpResponse
from django.db.models import Q
from django.contrib import messages

# Create your views here.
def main(request):
    if request.method == 'POST':
        Location = request.POST['Location']
        Incident_Desc = request.POST['Incident_Desc']
        Incident_Loc = request.POST['Incident_Loc']
        Date = request.POST['Date']
        Time = request.POST['Time']
        Initial_Security = request.POST['Initial_Security']
        Suspected_Cause = request.POST['Suspected_Cause']
        Actions = request.POST['Actions']
        Incident_Type = request.POST['Incident_Type']
        Reported_by = request.POST['Reported_by']
        data = Forms(Location = Location, Incident_Desc = Incident_Desc, Incident_Loc = Incident_Loc, Date = Date, Time = Time,
                          Initial_Security = Initial_Security, Suspected_Cause = Suspected_Cause, Actions = Actions,
                        Incident_Type = Incident_Type, Reported_by = Reported_by)
        data.save()
        return redirect('main')
    else:
        return render(request,'main.html')