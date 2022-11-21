from django.db import models

# Create your models here.

class Pricing(models.Model):
    id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=50)
    distance = models.FloatField(null=False,blank=False)
    time_taken = models.TimeField(null=False,blank=False)
    total_price = models.FloatField(null=False,blank=False,default=0)