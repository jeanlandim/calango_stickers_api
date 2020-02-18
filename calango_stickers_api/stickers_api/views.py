from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .models import StickersModels
from .serializers  import StickersSerializer
from .filters import StickersFilter

class StickersApiList(generics.ListCreateAPIView):
    queryset = StickersModels.objects.all()
    serializer_class = StickersSerializer
    filters_backend = [DjangoFilterBackend]
    filterset_fields = '__all__' 
class StickersApiListItems(generics.RetrieveUpdateDestroyAPIView):
    queryset = StickersModels.objects.all()
    serializer_class = StickersSerializer

def stickers(request):
    return render(request,'index.html')
