# sku app views.py
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template import loader, Context
from debug_site.sku.models import Sku
from django.template import RequestContext



def ver(request, sku_id):
    '''
    Accepts a sku ID and returns the detail page
    Only availiable for authenticaded users 
    '''
    p = get_object_or_404(Sku, id=sku_id)
    if request.user.is_authenticated():
        t = loader.get_template('sku-ver.html')
        c = RequestContext( request, ({'sku': p}))
        return HttpResponse(t.render(c))
    else:
        #t = loader.get_template('sku-redirect-login.html')
        #c = RequestContext( request, ({'sku': p}))
        #return HttpResponse(t.render(c))
        return HttpResponseRedirect('/admin/')
