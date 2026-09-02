

from django.shortcuts import render
from .models import Drinks
from .serializers import DrinkSerializer

from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



# Create your views here.


@api_view('GET', 'POST')


def drink_list(request):

    if request.method == 'GET':
        drinks = Drinks.objects.all()
        serializer = DrinkSerializer(drinks, many = True)
        return JsonResponse({'drinks':serializer.data}, safe = False)


    if request.method == 'POST':
        serializer = DrinkSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)