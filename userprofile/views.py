from datetime import datetime

from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response

from .models import UserProfile
from .serializers import UserProfileSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()

    filter_fields = [
        "uid",
    ]

    search_fields = [
        "uid",
    ]

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    ordering_fields = ["uid"]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, **kwargs):
        guid = request.query_params.get("uid", None)
        if guid is not None:
            profile = get_object_or_404(UserProfile, uid=guid)
            return Response(
                status=status.HTTP_200_OK
                if UserProfile.objects.filter(
                    uid=guid, days_of_use__gte=datetime.now()
                ).count() > 0
                else status.HTTP_403_FORBIDDEN
                ,
                data=profile.days_of_use
            )
        return Response(status=status.HTTP_400_BAD_REQUEST)
