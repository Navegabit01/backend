from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Card
from .serializer import CardSerializer


class CardsViewSet(viewsets.ModelViewSet):
    """
        Api Cards Data.
    """
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_fields = ['id', 'title', 'text',
                        'active', 'url', 'order', 'type']
    search_fields = ['id', 'title', 'text',
                     'active', 'url', 'order', 'type']
    ordering_fields = '__all__'
