from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Translate_relation
from .serializer import Translate_relationSerializer


class TranslateViewSet(viewsets.ModelViewSet):
    """
        Api Translate Data.
    """
    queryset = Translate_relation.objects.all()
    serializer_class = Translate_relationSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_fields = ['id','translate', 'menu_translate', 'card_translate']
    search_fields = ['id', 'translate', 'menu_translate', 'card_translate']
    ordering_fields = '__all__'
# Create your views here.
