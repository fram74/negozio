__author__ = 'fram'

# URLconf
from django.conf.urls import url

urlpatterns = [
    url(r'^test/$', 'novita.views.list'),
]


from django.conf.urls import *

urlpatterns = patterns('novita.views',
    url(r'^$', 'list', name='app_main'),

)