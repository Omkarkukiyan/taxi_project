from django.db import models
from accounts.models import Account

class Trip(models.Model):
    REQUESTED = 'REQUESTED'
    IN_PROGRESS = 'IN_PROGRESS'
    COMPLETED = 'COMPLETED'
    STATUSES = (
        (REQUESTED, REQUESTED),
        (IN_PROGRESS, IN_PROGRESS),
        (COMPLETED, COMPLETED),
    )
    trip_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE,null=True, default=None)
    rider = models.ForeignKey(Account, related_name='rider', on_delete=models.CASCADE, null=True, blank=True)
    driver = models.ForeignKey(Account, related_name='driver', on_delete=models.CASCADE, null=True, blank=True)
    license_id = models.ForeignKey(Account, related_name='license',on_delete=models.CASCADE, null=True, blank=True)
    pickup = models.CharField(max_length=255)
    dropoff = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUSES, default=REQUESTED)


    def __str__(self):
        return f'{self.rider.first_name} {self.rider.last_name}'
    