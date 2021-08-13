from django.http import HttpResponse
from django.shortcuts import render
from .models import Reservation

def index(request):
    context = {
        'num_books': 2,
        'num_instances': 5,
        'num_instances_available': 4,
        'num_authors': 7,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)