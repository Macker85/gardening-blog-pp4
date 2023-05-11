from django.contrib import admin
from .models import Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_filter = (
        'user',
        'name',
        'email',
        'status',
        'requested_date',
    )
    list_display = (
        'user',
        'name',
        'email',
        'status',
        'requested_date',
    )
    summernote_fields = ('content')
    actions = ['confirm_appointment']

    def confirm_appointment(self, request, queryset):
        queryset.update(approved=True)
