from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import MenuItem
from .serializer import MenuSerializer


class HomeViewSet(viewsets.ModelViewSet):
    """
        Api Menu , Submenu, Item Data.
    """
    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_fields = ['name', 'url', 'parent', 'type']
    search_fields = ['id', 'name', 'url', 'parent', 'type']
    ordering_fields = '__all__'
