from rest_framework import routers
from .views import CardsViewSet

cards_patterns = routers.DefaultRouter()
cards_patterns.register(r'', CardsViewSet, basename='ServicesViewSet')
