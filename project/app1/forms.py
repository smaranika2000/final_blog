from django import forms

class Appointment(forms.Form):
    required_specialist = forms.CharField( max_length=100, required=True)
    apointment_date = forms.DateField(required=True)
    appointment_stime= forms.DateTimeField(required=True)