from django.shortcuts import render
from django.views import View, generic
from django.contrib import messages
from django.contrib.auth.models import User


class ContactRequest(View):
    template_name = 'contact.html'

    def post(self, request):
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            contact = contact_form.save(commit=False)
            contact.user = request.user
            contact.save()
            messages.success(request, "Message sent, you should get a repsonse soon")
            return render(request, 'contact_approved.html')

        return render(request, 'contact.html', {contact_form: contact_form})
