from django.db import models

class Listing(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='USD')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image_urls = models.TextField(null=True, blank=True)
    ratings = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    description = models.TextField(null=True, blank=True)
    reviews = models.IntegerField(default=0)
    amenities = models.TextField(null=True, blank=True)
    host_info = models.TextField(null=True, blank=True)
    property_type = models.CharField(max_length=100, default='Apartment')

    def __str__(self):
        return self.title