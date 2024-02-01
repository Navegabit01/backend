from rest_framework import routers
from .views import HomeViewSet

menu_patterns = routers.DefaultRouter()
menu_patterns.register(r'', HomeViewSet, basename='HomeViewSet')
