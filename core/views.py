from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. parte logica de cada pagin

def sobre(request):
    return render(request, "index.html")