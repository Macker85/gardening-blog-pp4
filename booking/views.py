from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import Booking
from .forms import BookingForm


def get_user_instance(request):
    """
    retrieves user details if logged in
    """

    user_email = request.user.email
    user = User.objects.filter(email=user_email).first()
    return user


class Facetime(View):
    template_name = 'bookings.html'

    def get(self, request, *args, **kwargs):
        """
        Retrieves users email and inputs into email input
        """
        if request.user.is_authenticated:
            email = request.user.email
            booking_form = BookingForm(initial={'email': email})
        else:
            booking_form = BookingForm()
        return render(request, 'bookings.html',
                      {'booking_form': booking_form})
