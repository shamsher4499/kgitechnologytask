from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def home(request):
    template = 'templates/home.html'
    return render(request, template)


def registration_form(request):
    if request.method == 'POST':
        form = VehicalForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
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

# def test(request):
#     template = 'templates/index.html'
#     return render(request, template)

def test(request):
    if request.method == 'POST':
        form = VehicalForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form = VehicalForm()
    template = 'templates/index.html'
    return render(request, template)

def registration_info(request):
    register = VehicleGeneralForm.objects.all()
    template = 'templates/basic-table.html'
    return render(request, template, {'register':register})


def user_data(request, aid):
    application = VehicleGeneralForm.objects.get(id=aid)
    template = 'templates/user-data.html'
    return render(request, template, {'application':application})


def contact_us(request):
    template = 'templates/contactus.html'
    return render(request, template)