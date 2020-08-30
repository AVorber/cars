from django.db import models
from django.utils.datetime_safe import datetime
from django.utils.text import slugify


class Car(models.Model):
    BRAND_CHOICES = [
        ('Skoda', 'Skoda'),
        ('BMW', 'BMW'),
        ('Audi', 'Audi'),
        ('Mercedes', 'Mercedes')
    ]
    TRANSMISSION_CHOICES = [
        (1, 'Manual'),
        (2, 'Automatic'),
        (3, 'Robot')
    ]
    YEAR_CHOICES = []
    COLOR_CHOICES = [
        ('Red', 'Red'),
        ('Black', 'Black'),
        ('White', 'White'),
        ('Grey', 'Grey'),
        ('Green', 'Green'),
    ]
    for year in range(1980, datetime.now().year):
        YEAR_CHOICES.append((year, year))
    brand = models.CharField(max_length=255, choices=BRAND_CHOICES)
    model = models.CharField(max_length=255)
    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.now().year)
    transmission = models.SmallIntegerField(choices=TRANSMISSION_CHOICES)
    color = models.CharField(max_length=255, choices=COLOR_CHOICES)
    image = models.ImageField(upload_to='media', default='defaultCar.jpg')
    slug = models.SlugField(blank=True, unique=True, max_length=200)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.brand)
        super(Car, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.brand} {self.model} {self.year}'
