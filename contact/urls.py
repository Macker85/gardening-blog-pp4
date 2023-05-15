from contact import views
from django.urls import path

urlpatterns = [
    path('', views.ContactRequest.as_view(), name='contact'),
]