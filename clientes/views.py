from django.shortcuts import render
from .serializers import ClientesSerializer
from .models import Clientes
from rest_framework import generics, permissions


class ClientesViewSet(generics.ListCreateAPIView):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer
    # permission_classes = ()

clientelist = ClientesViewSet.as_view()


