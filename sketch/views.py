from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def simple_view(request):
    return HttpResponse('You made it to the end')
