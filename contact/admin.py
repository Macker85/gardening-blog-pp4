from django.contrib import admin
from .models import Contact
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_filter = (
        'email',
        'name',
        'user',
        'created_date'
        )
    list_display = (
        'message_id',
        'name',
        'user',
        'message',
        'created_date')
    summernote_fields = ('message')