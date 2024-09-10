from django.shortcuts import render
from django.http import HttpResponse


def index(request):
 
    
    return render(request, 'books/index.html')

def show(request, id):

    return render(request, 'books/show.html')