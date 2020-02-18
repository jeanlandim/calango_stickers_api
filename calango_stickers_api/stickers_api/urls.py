from .views import *
from django.urls import path, include

urlpatterns = [
        path('stickers-api/',StickersApiList.as_view(),name='stickers-api'),
        path('stickers-api/<pk>',StickersApiListItems.as_view(),name='stickers-api'),
        path('', stickers, name='stickers')
]
