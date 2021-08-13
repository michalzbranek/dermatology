import datetime
import logging
import pymongo

from django.http import HttpResponse
from django.shortcuts import render
from .models import Reservation
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from derma.forms import ReservationForm
from pymongo import MongoClient

def index(request):
    return render(request, 'index.html')

def make_booking(request):
    # form = ReservationForm(request.POST)
    omg = Reservation()
    omg.name = request.POST.get('name')
    omg.phone = request.POST.get('phone')
    omg.email = request.POST.get('email')

    client = MongoClient("mongodb+srv://BliXer:stfumiabot268@blog.47rde.mongodb.net/dermatology?retryWrites=true&w=majority")
    logging.critical('DATABASE DATABASE DATABASE')
    db = client.dermatology
    db.reservation.insert_one({"name":"michal"})

    return render(request, 'index.html')