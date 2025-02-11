from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import Author
from .serializer import AuthorSerializer
from rest_framework.decorator import api_view

# Create your views here.


@api_view()
def main(request):
    return response({"message": "Hello World", status.HTTP_200_OK})
