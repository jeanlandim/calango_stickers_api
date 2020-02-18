from rest_framework import serializers
from .models import StickersModels

class StickersSerializer(serializers.ModelSerializer):
    class Meta:
        model = StickersModels
        fields = ('sticker_name','sticker_description','sticker_quantity')
