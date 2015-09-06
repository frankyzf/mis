from django.db import models

# Create your models here.

class server(models.Model):
	name = models.CharField(max_length=64)
	ipaddress = models.GenericIPAddressField()
	login = models.CharField(max_length=64, default='sellside')
	password = models.CharField(max_length=64, default='Flex123!')
	volumefolder= models.CharField(max_length=256, default='/home/sellside/fx-client-volumes/daily-rpts')
	class Meta:
		ordering = ['name']


class volume(models.Model):
    date = models.DateField('trade date')
    time = models.TimeField('trade time')
    side = models.CharField(max_length=8)
    symbol = models.CharField(max_length=64)
    bank = models.CharField(max_length=64)
    size = models.IntegerField()
    price = models.FloatField()
    termsize = models.FloatField()
    server = models.CharField(max_length=64)

class process(models.Model):
    server = models.CharField(max_length=64)
    date = models.DateField('processed_date')