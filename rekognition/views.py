from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from . import utils

def index(request):
    return render(request, 'index.html')

def submit(request):
    response = utils.detect_faces(request.body)
    return JsonResponse(response)