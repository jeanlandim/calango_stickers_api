from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from .models import StickersModels
from .serializers  import StickersSerializer
from .filters import StickersFilter

from django.http import JsonResponse
from jsonrpcserver import method, dispatch

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

# jsonrpcserver statements

@method 
def ls(): # list stickers available
    stickers = []
    for sticker in StickersModels.objects.values():
        if sticker['sticker_quantity'] => 1:
           stickers.append(sticker['sticker_name']) 
    return(stickers)

@method 
def cat(such_sticker): # get description of stickers 
    stickers_description = '' 
    for sticker in StickersModels.objects.values():
        if sticker['sticker_quantity'] => 1:
           stickers_description = sticker['sticker_description'] 

    return(stickers_description)


    
