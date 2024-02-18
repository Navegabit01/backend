from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import UserProfile
from .serializers import UserProfileSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.response import Response


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

    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())

    #     # Realizamos alguna manipulación adicional en el queryset si es necesario
    #     # Por ejemplo, filtrar los objetos por algún criterio específico
    #     filtered_queryset = queryset.filter(uid=request.get())

    #     page = self.paginate_queryset(filtered_queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)

    #     serializer = self.get_serializer(filtered_queryset, many=True)
    #     return Response(serializer.data)

    def list(self, request):
        # Retrieve the GUID parameter from the request query parameters
        guid = request.query_params.get("uid", None)
        if guid is not None:
            # If a GUID parameter is provided, filter the queryset by GUID
            queryset = UserProfile.objects.filter(uid=guid)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        #     # If no GUID parameter is provided, return all users
        #     queryset = UserProfile.objects.all()

        serializer = UserProfileSerializer(queryset, many=True)
        # Serialize the queryset

        # Return the serialized data
        return Response(serializer.data)
