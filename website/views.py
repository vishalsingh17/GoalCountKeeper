from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.renderers import TemplateHTMLRenderer
from website.models import PlayerTable, ChildTable
from .serializers import PlayerTableSerializer, ChildTableSerializer
from rest_framework import generics,filters,viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
# Create your views here.
class PlayerView(generics.ListAPIView):
    serializer_class = PlayerTableSerializer
    filter_backends = (DjangoFilterBackend,SearchFilter)
    search_fields 	  = ('player_name',)
    queryset = PlayerTable.objects.all()


class ChildView(generics.ListAPIView):
    queryset = ChildTable.objects.all()
    serializer_class = ChildTableSerializer

class Homepage(APIView):
	def get(self, request):

		return render(request, 'Homepage.html')

class chart_view(APIView):
    def get(self, request):
        return render(request, 'graphview.html')
