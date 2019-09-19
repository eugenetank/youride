from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rides.models import Car
from rides.serializers import CarSerializer

@api_view(['GET', 'POST'])
def cars_list(request,  format=None):
    """
    List all code snippets, or create a new snippet
    :param request:
    :return:
    """
    if request.method == 'GET':
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # data = JSONParser().parse(request)
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def car_detail(request, pk, format=None):
    """
    Retrieve, update or delete a car.
    :param request:
    :param pk:
    :return:
    """
    try:
      car = Car.objects.get(pk=pk)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CarSerializer(car)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
