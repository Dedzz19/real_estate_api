from django.db import models
from user_app.models import Agent
# Create your models here.


PROPERTY_TYPES = [
    ('Land', 'Land'),
    ('House', 'House'),
    ('Flat/Apartment', 'Flat/Apartment'),
    ('Commercial Property', 'Commercial Property'),
]

REGIONS=[
    ('Lagos','Lagos'),
    ('Abuja','Abuja'),
    ('Ogun','Ogun'),
    ('Edo','Edo'),
]

class Property(models.Model):
    title=models.CharField(max_length=100)
    address = models.TextField()
    description = models.TextField()
    property_type=models.CharField(max_length=100,choices=PROPERTY_TYPES)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    state=models.CharField(max_length=100, choices=REGIONS, default="Lagos")
    agent=models.ForeignKey(Agent,on_delete=models.CASCADE, related_name="property")
    def __str__(self):
       return f'{self.title} by {self.agent}'
    

class PropertyImage(models.Model):
    property= models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images', null=True, blank=True)
    image = models.ImageField(upload_to='property_images/')

    def __str__(self):
        return f"{self.property.title}"