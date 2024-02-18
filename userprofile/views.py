from datetime import datetime, timedelta
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import UserProfile
from .serializers import UserProfileSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


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
        # Crear una instancia del serializador con los datos de la petición
        serializer = self.get_serializer(data=request.data)

        # Validar los datos
        if serializer.is_valid():
            # Si los datos son válidos, guardar el objeto en la base de datos
            serializer.save()
            # Retornar una respuesta con el objeto creado y el código de estado HTTP 201
            return Response(serializer.data, status=status.HTTP_201_CREATED)

            # Si los datos no son válidos, retornar una respuesta con los errores y el código de estado HTTP 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        guid = request.query_params.get("uid", None)
        if guid is not None:
            get_object_or_404(UserProfile, uid=guid)
            return Response(
                status=status.HTTP_200_OK
                if UserProfile.objects.filter(
                    uid=guid, days_of_use__gte=datetime.now()
                ).count()
                > 0
                else status.HTTP_403_FORBIDDEN
            )
        return Response(status=status.HTTP_400_BAD_REQUEST)
