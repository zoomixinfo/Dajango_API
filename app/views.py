from django.shortcuts import render
from django.http import HttpResponse
import requests


def index(request):
    response = requests.get('https://inshorts.deta.dev/news?category=science')
    posts = response.json()
    data = posts['data']
    return render(request, 'index.html', {'posts': data})
    #return HttpResponse("Hello, world. You're at the polls index.")
