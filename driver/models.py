from django.db import models
from django.core.validators import RegexValidator

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')



# Create your models here.
class DriversAllTrips(models.Model):
    driver_email = models.EmailField()
    rider_first_name = models.CharField(max_length=255, blank=True)
    rider_last_name = models.CharField(max_length=255, blank=True)
    rider_profile_pic = models.ImageField()
    rider_email=models.EmailField()
    driver_license_id = models.CharField(max_length=10, validators=[alphanumeric], blank=True)
    pickup = models.CharField(max_length=255)
    dropoff = models.CharField(max_length=255)
    status = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.driver_email}'
    
