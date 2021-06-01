from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def home(request):
    template = 'templates/registration.html'
    return render(request, template)


def registration_form(request):
    if request.method == 'POST':
        form = VehicalForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = VehicalForm()
    template = 'templates/registration.html'
    return render(request, template)


def registration_details(request):
    register = VehicleGeneralForm.objects.all()
    template = 'templates/details.html'
    return render(request, template, {'register':register})

def reguster_user(request):
    register = VehicleGeneralForm.objects.all()
    template = 'templates/register_user.html'
    return render(request, template, {'register':register})