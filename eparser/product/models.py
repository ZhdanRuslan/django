from django.db import models


class Vacancy(models.Model):
    initial = True

    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    description = models.TextField(max_length=2048)
    city = models.CharField(max_length=50)
    contact = models.CharField(max_length=50, default='0000000')

    def __str__(self):
        return '{} in {}'.format(self.position, self.company)
