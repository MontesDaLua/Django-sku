# sku app urls.py
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^ver/(?P<sku_id>\d+)/$', 'sku.views.ver'),
)

