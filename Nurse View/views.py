from django.utils import timezone
from .models import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.forms import forms
from django.contrib.auth import authenticate, login
from django.forms import forms



"""

def home(request):
    return render(request, 'nurseView/nurse_home.html',
                  {'nurseView': home})

"""

def nurse_home(request):
    return render(request, 'nurseView/nurse_home.html',
                  {'nurseView': nurse_home})

@login_required()
def patient_list(request):
        return render(request, 'nurseView/patient_list.html',
                      {'form': patient_list})


def patient_det(request):
        return render(request, 'nurseView/patient_det.html',
                      {'form': patient_det})
