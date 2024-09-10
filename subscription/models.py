from django.db import models
from accounts.models import CustomUser

class subscriptionplan(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    duration_in_days = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class subscription(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    plan = models.ForeignKey(subscriptionplan, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.user} - {self.plan}'
    
