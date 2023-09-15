from django.db import models

class Property(models.Model):
    name = models.CharField(max_length=255)
    cost = models.CharField(max_length=100)
    property_type = models.CharField(max_length=100)  
    area = models.CharField(max_length=100)
    locality = models.CharField(max_length=255) 
    link = models.URLField(max_length=500)


    def __str__(self):
        return self.name