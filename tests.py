"""
unittest for Sku module 
"""

from django.utils import unittest
from models import Sku
from django.test import TestCase

class SkuTestCase(unittest.TestCase):
    def setUp(self):
        self.sku1 = Sku.objects.create( IntCode = "Codigo 1", MovUnit = '', Desc = "Descricao Codigo 1", ShortDesc = "Descricao Curta Codigo 1") 
    	self.sku1.LoadSampleData(10)

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
    def testWst3(self):
        """
        Test sky object single creation 
        """
