from django.db import models

class ClimateData(models.Model):
    year = models.IntegerField()
    month = models.CharField(max_length=10)
    value = models.FloatField()
    parameter = models.CharField(max_length=100)
    region = models.CharField(max_length=100)

    class Meta:
        unique_together = ['year', 'month', 'parameter', 'region']
        
    def __str__(self):
      return f"{self.region}-{self.parameter}-{self.year}-{self.month}"
        
    # def __str__(self):
    #   return self.region