# Generated by Django 3.2.3 on 2023-05-13 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_alter_booking_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('Confirmation pending', 'Confirmation pending'), ('Booking Confirmed', 'Booking Confirmed'), ('Unavailable', 'Unavailable')], default='Confirmation pending', max_length=25),
        ),
    ]
