from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import VehicleForm

def home(request):
  form = VehicleForm()

  if request.method == 'POST':
    form = VehicleForm(request.POST)

    if form.is_valid():
      form.save()
      return HttpResponse("Success")
    
  return render(request, 'index.html', {'form': form})