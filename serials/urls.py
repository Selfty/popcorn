from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	url(r'^(?P<name>[\w]+)/(?P<sn>[0-9]+)/(?P<en>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'^serials/$', views.serials, name='serials'),
	url(r'^serial/(?P<name>[\w]+)/$', views.serial, name='serial')
]
