from django import forms

class ReservationForm(forms.Form):
    name = forms.CharField()
    phone = forms.CharField()
    email = forms.CharField()
    time = forms.DateTimeField()