from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

times = (
    ('18:00', '18:30'),
    ('18:30', '19:00'),
    ('19:00', '19:30'),
    ('19:30', '20:00'),
    ('20:00', '20:30'),
)

days = (
    ('Monday'),
    ('Tuesday'),
    ('Wednesday'),
    ('Thursday'),
    ('Friday'),
)

status_options = (
    ('Confirmation pending', 'Confirmation pending'),
    ('Booking Confirmed', 'Booking Confirmed'),
    ('Unavailable', 'Unavailable'),
)


class Booking(models.Model):
    """
    a class for the Booking model
    """
    booking_id = models.AutoField(primary_key=True)
    booked_date = models.DateTimeField(auto_now_add=True)
    requested_date = models.DateField()
    requested_time = models.CharField(
        max_length=30,
        choices=times,
        default='18:00',
        )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user", null=True)
    name = models.CharField(
        max_length=50,
        null=True
        )
    email = models.EmailField(
        max_length=100,
        default=""
        )
    status = models.CharField(
        max_length=25,
        choices=status_options,
        default='Confirmation pending'
        )

    class Meta:
        ordering = ['-requested_time']

    def __str__(self):
        return self.status
