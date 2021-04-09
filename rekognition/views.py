from django.shortcuts import render
from django.http import JsonResponse

from . import utils

def index(request):
    utils.detect_faces('test')
    context = {'test': 'test message'}
    return render(request, 'index.html', context)