from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from mysite.models import About
from mysite.serializers import AboutSerializer

from rest_framework import status, views, generics, viewsets
from rest_framework.parsers import JSONParser
from rest_framework.response import Response


# Create your views here.


class AboutViewSet(viewsets.ReadOnlyModelViewSet):
    """ AboutモデルのCRUD用APIクラス、ただし、read only """
    queryset = About.objects.get(id=1)
    serializer_class = AboutSerializer
