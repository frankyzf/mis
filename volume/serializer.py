from volume.models import server,volume
from rest_framework import serializers

class ServerSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = server
		fields = ('name', 'ipaddress')

class VolumeSerializer(serializers.ModelSerializer):
	class Meta:
		model = volume

