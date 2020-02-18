import django_filters 
from .models import StickersModels

class StickersFilter(django_filters.FilterSet):
    class Meta:
        model = StickersModels
        fields = '__all__'
