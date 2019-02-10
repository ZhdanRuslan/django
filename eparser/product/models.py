from django.db import models

# Create your models here.
class Phone(models.Model):

    initial = True

    brand = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    year = models.IntegerField(max_length=255)
    model = models.CharField(max_length=255)
    price = models.FloatField(max_length=255)

    def __str__(self):
        return 'Brand - {} Name - {} Version -  {}, price - {}'.format(self.brand, self.name, self.model, self.price)