# sku app urls.py
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^versku/(?P<sku_id>\d+)/$', 'sku.views.versku'),
)

