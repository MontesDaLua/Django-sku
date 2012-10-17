"""
unittest for Sku module 
"""

from django.utils import unittest
from django.test import TestCase
from django.test.client import RequestFactory, Client 
from django.contrib.auth.models import User
from models import Sku

class SkuTestCase(unittest.TestCase):
    def setUp(self):
        self.sku1 = Sku.objects.create( IntCode = "Codigo 1", MovUnit = '', Desc = "Descricao Codigo 1", ShortDesc = "Descricao Curta Codigo 1") 
        self.sku1.LoadSampleData(10)
        self.c = Client()


#
# Database Tests 
#

    def testDbSku(self):
        """
        Test sky object single creation 
        """
        self.assertEqual(self.sku1.IntCode, 'Codigo 1')

    def testDbLoadSku(self):
        """
        Test sky object single creation 
        """

    def testDbt3(self):
        """
        Test sky object single creation 
        """
#
# Web site tests
#
    def testWst1(self):
        """
        Authentication
        """
        self.assertEqual( self.c.login(username='fred', password='secret'), False)
        self.uname = 'okuser'
        self.PASS = 'lixo'
	User.objects.create_user(self.uname, "ll@datreta.com", self.PASS)
        self.assertEqual( self.c.login(username=self.uname, password=self.PASS), True )

    def testWst2(self):
        """
        Defined Views
        """
	#
	# generic 
	r = self.c.get('/sku/')
        self.assertEqual( r.status_code, 404  )
	#
	# Existing sku
	r = self.c.get('/sku/ver/'+ str(self.sku1.id) +'/')
        self.assertEqual( r.status_code, 200  )
	#
	# Non Existing sku
	r = self.c.get('/sku/ver/5555/')
        self.assertEqual( r.status_code, 404  )
	
