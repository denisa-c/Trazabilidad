from django.shortcuts import render
from models import Lote


def index(request):
    return render(request, 'base.html')
