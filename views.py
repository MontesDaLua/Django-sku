# sku app views.py
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template import loader, Context
from debug_site.sku.models import Sku
from django.template import RequestContext
from django.utils import translation




def versku(request, sku_id):
    '''
    Accepts a sku ID and returns the detail page
    Only availiable for authenticaded users 
    '''
    p = get_object_or_404(Sku, id=sku_id)
    if request.user.is_authenticated():
        t = loader.get_template('sku-versku.html')
        c = RequestContext( request, ({
           'sku': p, 
           #'msg': translation.get_language()
           'msg': request.LANGUAGE_CODE
            }))
        return HttpResponse(t.render(c))
    else:
        return HttpResponseRedirect('/admin/')
