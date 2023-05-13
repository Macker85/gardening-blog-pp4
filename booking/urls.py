from . import views
from django.urls import path


urlpatterns = [
    path('', views.Facetime.as_view(), name='bookings'),
]