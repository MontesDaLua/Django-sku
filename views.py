# sku app views.py
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import loader, Context
from debug_site.sku.models import Sku
from django.template import RequestContext



def ver(request, sku_id):
    '''
    Accepts a sku ID and returns the detail page
    '''
    p = get_object_or_404(Sku, id=sku_id)
    t = loader.get_template('sku-ver.html')
    c = RequestContext( request, ({'sku': p}))
    return HttpResponse(t.render(c))
