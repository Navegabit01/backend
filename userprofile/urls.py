from rest_framework import routers
from .views import UserProfileViewSet

userprofile_patterns = routers.DefaultRouter()
userprofile_patterns.register(r'', UserProfileViewSet, basename='UserViewSet')
