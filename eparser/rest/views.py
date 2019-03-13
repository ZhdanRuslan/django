from rest_framework import viewsets

from product.models import Vacancy
from .serializers import VacancySerializer


class VacancyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows vacancies to be viewed or edited.
    """
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
