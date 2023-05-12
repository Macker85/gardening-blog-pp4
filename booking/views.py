from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Booking
from .forms import BookingForm


class Facetime(View):
    template_name = 'booking/'
    success_message = 'I look forward to chatting with you!'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            email = request.user.email
            booking_form = BookingForm(initial={'email': email})
        else:
            return render(request, 'account_login')