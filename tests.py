"""
unittest for Sku module 
"""

from django.utils import unittest
from django.test import TestCase
from django.test.client import RequestFactory, Client 
from django.contrib.auth.models import User
from models import Sku
import os

class SkuTestCase(unittest.TestCase):
    def setUp(self):
        self.sku1 = Sku.objects.create( IntCode = "Codigo 1", MovUnit = '', Desc = "Descricao Codigo 1", ShortDesc = "Descricao Curta Codigo 1") 
        self.c = Client()
        self.uname = 'okuser'
        self.PASS = 'lixo'
	self.baseurl = '/sku/'
	self.viewurl = 'versku/'

#
# Database Tests 
#

    def testDbt1(self):
        """
        Test sky object single creation 
        """
        self.assertEqual(self.sku1.IntCode, 'Codigo 1')

#
# Web site tests
#
    def testWst1(self):
        """
        Authentication
        """
        self.assertEqual( self.c.login(username='fred', password='secret'), False)
	User.objects.create_user(self.uname, "ll@datreta.com", self.PASS)
        self.assertEqual( self.c.login(username=self.uname, password=self.PASS), True )

    def testWst2(self):
        """
        Defined sku Views
        """
	#
	# generic 
	r = self.c.get(self.baseurl)
        self.assertEqual( r.status_code, 404  )
	#
	# Existing sku non authenticated 
	r = self.c.get(self.baseurl + self.viewurl + str(self.sku1.id) +'/')
        self.assertEqual( r.status_code, 302  )
	#
	# Existing sku authenticated 
	self.c.login(username=self.uname, password=self.PASS)
	r = self.c.get(self.baseurl + self.viewurl + str(self.sku1.id) +'/')
        self.assertEqual( r.status_code, 200  )
	of =  os.environ['APPTESTNAME'] + '/' + os.environ['APP'] + '/' + os.environ['APPSNAPHTMLDIR'] + '/' + 'versku-200.html'
	self.c.logout()
	fwrite = open( of ,'w')
	fwrite.write (r.content);
	fwrite.close()
	#
	# Non Existing sku
	r = self.c.get(self.baseurl + self.viewurl + '5555/')
        self.assertEqual( r.status_code, 404  )
	
    def testWst3(self):
        """
        admin login  View
        """
	#
	# generic 
	r = self.c.get('/admin/')
        self.assertEqual( r.status_code, 200  )
	of =  os.environ['APPTESTNAME'] + '/' + os.environ['APP'] + '/' + os.environ['APPSNAPHTMLDIR'] + '/' + 'admin.html'
	fwrite = open( of ,'w')
	fwrite.write (r.content);
	fwrite.close()
