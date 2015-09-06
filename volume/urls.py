from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'server$', views.ServerList.as_view()),
	url(r'volume$', views.VolumeList.as_view()),

]