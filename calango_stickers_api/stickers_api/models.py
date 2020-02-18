from django.db import models

class StickersModels(models.Model):
    sticker_name = models.CharField(max_length = 20)
    sticker_description = models.TextField()
    sticker_quantity = models.IntegerField()






