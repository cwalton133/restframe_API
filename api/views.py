#import response
from rest_framework.response import Response
from rest_framework import status
from .models import Author
from .serializer import AuthorSerializer
from rest_framework.decorators import api_view


# Create your views here.


@api_view()
def main(request):
    return Response({"message": "Hello World", "status": status.HTTP_200_OK})
