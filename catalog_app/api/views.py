from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from catalog_app.models import Car
from .serializers import CarSerializer


@api_view(['GET'], )
def api_detail_car_view(request, slug):
    try:
        car = Car.objects.get(slug=slug)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CarSerializer(car)
        return Response(serializer.data)
