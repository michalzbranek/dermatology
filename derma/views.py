from django.shortcuts import render
from pymongo import MongoClient

def booking(request):
    if request.method == 'POST':
        client = MongoClient("mongodb+srv://BliXer:stfumiabot268@blog.47rde.mongodb.net/dermatology?retryWrites=true&w=majority")
        db = client.dermatology

        if request.POST.get('reservation') == 'Rezervace':
            db.reservation.update(
                {'name': request.POST.get('name')},
                {
                    "name": request.POST.get('name'),
                    "phone": request.POST.get('phone'),
                    "email": request.POST.get('email')
                },
                upsert = True
            )
        else:
            db.reservation.remove(
                {
                    "name": request.POST.get('name'),
                    "phone": request.POST.get('phone'),
                    "email": request.POST.get('email')
                },
                multi = False
            )

        return render(request, 'index.html')
    else:
        return render(request, 'index.html')

def remove_booking(request):
    if request.method == 'POST':
        client = MongoClient("mongodb+srv://BliXer:stfumiabot268@blog.47rde.mongodb.net/dermatology?retryWrites=true&w=majority")
        db = client.dermatology

        

        return render(request, 'index.html')
    else:
        return render(request, 'index.html')