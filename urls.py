# sku app urls.py
from django.conf.urls.defaults import *

#export APPSTRVIEW="ver"

urlpatterns = patterns('',
    url(r' ver/(?P<pid>\d+)/$', 'sku.views.ver'),
)

