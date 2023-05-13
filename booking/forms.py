from django import forms
from crispy_forms.helper import FormHelper
from .models import Booking
from datetime import datetime

# Booking form for Factime for gardening support


class BookingForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    # requested_date = forms.DateField(
    #     widget=forms.DateField(
    #         attrs={'type': 'date', 'min': datetime.now().date()}))
    
    class Meta:
        model = Booking
        fields = (
            'name',
            'email',
            'requested_date',
            'requested_time',
        )