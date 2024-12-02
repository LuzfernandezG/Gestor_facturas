from django.shortcuts import render
from django.http import HttpResponse,response,JsonResponse
# from rich.console import Console
# console = Console()

# from .models import (
#     Categoria,
#     Productos
# )
# Django Rest Framework
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import IsAuthenticated


class Facturas(APIView):

    def get(self, request):

        return Response({"Facturas":"Hola:)"}, status=status.HTTP_200_OK)
 