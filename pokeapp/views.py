from django.http.response import HttpResponse
from django.shortcuts import render
import requests

# Create your views here.

def index(request, pk):
    response = requests.get('https://pokeapi.co/api/v2/evolution-chain/1/').json()

    return HttpResponse(response['chain']['species']['name'])