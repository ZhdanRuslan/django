from product.models import Vacancy

from rest_framework import serializers

class VacancySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('company', 'position', 'description')
