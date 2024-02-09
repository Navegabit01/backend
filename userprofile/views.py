from rest_framework.filters import SearchFilter
from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework import viewsets, filters

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    
    # filter_backends = [
    #     DjangoFilterBackend,
    #     filters.SearchFilter,
    #     filters.OrderingFilter
    # ]
    # filterset_fields = ['id', 'title', 'text',
    #                     'active', 'url', 'order', 'type']
    # search_fields = ['id', 'title', 'text',
    #                  'active', 'url', 'order', 'type']
    # ordering_fields = '__all__'