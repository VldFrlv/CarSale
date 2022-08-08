from django.db import models
from django.urls import reverse_lazy

from .choises import *
from accounts.models import CustomUser


class Car(models.Model):
    """Creating a car model"""
    type_of_venc = models.CharField('Type of venc', max_length=30, choices=type_of_venc_choice)
    brand = models.CharField('Brand', max_length=150, choices=brands_choice)
    model = models.CharField('Model', max_length=150)
    fuel = models.CharField('Type of fuel', max_length=30, choices=fuel_choice)
    engine_volume = models.DecimalField(max_digits=2, decimal_places=1, blank=True)
    transmission = models.CharField('Transmission', choices=transmission_choice, max_length=30)
    drive = models.CharField('Drive', choices=drive_choice, max_length=30)
    year = models.PositiveIntegerField('Year of car manufacture')
    color = models.CharField('Color', max_length=50)
    price = models.PositiveIntegerField('Price')
    price_currency = models.CharField('Currency', choices=currency_choice, max_length=30)
    mileage = models.IntegerField('Mileage')
    description = models.TextField('Description')
    photo_1 = models.ImageField('Photo', upload_to='media/photo/%Y/%m/%d/')
    photo_2 = models.ImageField('Photo', upload_to='media/photo/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField('Photo', upload_to='media/photo/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField('Photo', upload_to='media/photo/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField('Photo', upload_to='media/photo/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField('Photo', upload_to='media/photo/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField('Created date', auto_now_add=True)
    views = models.PositiveIntegerField('Views', default=0)
    seller = models.ForeignKey(CustomUser, on_delete=models.PROTECT, blank=True)

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

    def __str__(self):
        return f'{self.brand} {self.model}'

    def get_absolute_url(self):
        return reverse_lazy('view_car', kwargs={'pk': self.pk})
