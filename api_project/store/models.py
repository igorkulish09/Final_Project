from django.db import models


class Order(models.Model):
    # Опис поля моделі Order
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()
