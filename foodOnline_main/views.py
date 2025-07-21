from django.http import HttpResponse
from django.shortcuts import render

def home(request):
  context = {
    'name': 'Charan',
    'age': 21
  }
  return render(request, 'home.html', context)