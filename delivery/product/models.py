from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Product(models.Model):
    name_product = models.CharField(max_length=200)
    count_product = models.IntegerField(default=0)
    destination_adress = models.CharField(max_length=200)
    date_delivery = models.DateTimeField('date delivery')
    status = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('product:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name_product
