from rest_framework import generics
from .models import Chamado
from .serializers import ChamadoSerializer

class ChamadoListCreateView(generics.ListCreateAPIView):
    queryset = Chamado.objects.all()
    serializer_class = ChamadoSerializer

class ChamadoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chamado.objects.all()
    serializer_class = ChamadoSerializer
