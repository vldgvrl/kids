from django.db import models
from django.utils import timezone

class Item(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField('date')
    description = models.CharField(max_length=1000)
    duaration = models.IntegerField(default=30)

    def current_time(self):
       self.date = timezone.now()
        

    

