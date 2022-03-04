#from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    # return render(request, 'recipes/home.html', context={
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Márcio Luis Dresch',
    })


def sobre(request):
    return render(request, 'recipes\sobre.html')
