

from rest_framework import serializers
from .models import Drinks


class DrinkSerializer(serializers.ModelSerializers):
    class Meta:
        model = Drinks
        field = ['id', 'name', 'description']