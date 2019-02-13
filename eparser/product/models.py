from django.db import models


class Phone(models.Model):
    initial = True

    brand = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    model = models.CharField(max_length=255)
    price = models.FloatField(max_length=255)

    def __str__(self):
        return 'Brand - {} Name - {} Version -  {}, price - {}'.format(self.brand, self.name, self.model, self.price)


class Laptop(models.Model):
    initial = True

    brand = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    model = models.CharField(max_length=255)
    price = models.FloatField(max_length=255)

    def __str__(self):
        return 'Brand - {} Name - {} Version -  {}, price - {}'.format(self.brand, self.name, self.model, self.price)


class Order(models.Model):
    initial = True

    customer = models.CharField(max_length=255)
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)

    def __str__(self):
        return 'Order № {}, Customer - {}, Phone - {} '.format(self.pk, self.customer, self.phone.name)


class Vacancy(models.Model):
    initial = True

    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    title = models.CharField(max_length=2048)

    # @classmethod
    # def create(cls, company, position, title):
    #     return cls(company, position, title)

