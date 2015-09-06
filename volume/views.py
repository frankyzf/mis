from django.shortcuts import render

# Create your views here.
from django.contrib.staticfiles.views import serve
from volume.models import server, volume
from volume.serializer import ServerSerializer, VolumeSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.parsers import JSONParser
import volume.tools as tools
import datetime
def index(request):
	return serve(request, 'html/index.html')

class ServerList(generics.ListCreateAPIView):
	queryset = server.objects.all()
	serializer_class = ServerSerializer

class VolumeList(APIView):
    """
    volume query and handle class
    """
    def get(self, request, format=None):
        print "recv a get request:"
        type = request.GET.get('type', None)
        date = request.GET.get('date', None)
        servers = request.GET.get('servlist', None)
        sdate = datetime.datetime.strptime(date, "%Y%m%d")
        print sdate
        if type == 'bymonth' and  date and servers:
            first_day, last_day = tools.get_month_day_range(sdate)
            first_day = first_day.strftime('%Y-%m-%d')
            last_day = last_day.strftime('%Y-%m-%d')
            ss = servers.split(',')
            for s in ss:
                tools.process_data(s, first_day)
            queryset = volume.objects.filter(date__range=[first_day, last_day]).filter(server__in=ss)
        else:
            queryset = volume.objects.all()

        serializer = VolumeSerializer(queryset, many=True)
        return Response(serializer.data)

