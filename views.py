# sku app views.py
from django.http import HttpResponse

def ver(request, pid):
    return HttpResponse('This is just a test.')

