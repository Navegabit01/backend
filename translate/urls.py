from rest_framework import routers
from .views import TranslateViewSet

translate_patterns = routers.DefaultRouter()
translate_patterns.register(r'', TranslateViewSet, basename='TranslateViewSet')