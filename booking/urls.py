from . import views
from django.urls import path


urlpatterns = [
    path('bookings', views.Facetime.as_view(), name='bookings'),
]