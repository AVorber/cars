from rest_framework import serializers
from catalog_app.models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'year', 'transmission', 'color', 'image']
