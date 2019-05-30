from django.db import models
from django.contrib.auth.models import User


class PropertyType(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Property(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    capacity = models.IntegerField(default=2)
    street = models.CharField(max_length=100)
    building = models.CharField(max_length=10)
    apartment = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=200)
    type = models.ForeignKey(PropertyType, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Properties'


class Booking(models.Model):
    property = models.ForeignKey(Property, on_delete=models.PROTECT)
    date_from = models.DateField()
    date_to = models.DateField()

    def __str__(self):
        return f'Booking in {self.property.name} from {str(self.date_from)} to {str(self.date_to)}'
