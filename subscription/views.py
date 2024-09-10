from django.shortcuts import render

def index(request):
    return render(request, 'subscription/index.html')
