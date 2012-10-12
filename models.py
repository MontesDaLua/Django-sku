from django.db import models

#UNI = 1
#VW = 2

class Sku(models.Model): 
    """
	base clase for SKu ( Stock Keeping Unit ) 
    """
    MOV_CHOICES = (
        ('UNI', 'Units'),
        ('VW',    'Variable Weight'),
    )
    IntCode = models.CharField(max_length=20) 
    MovUnit = models.CharField(max_length=3, choices = MOV_CHOICES , default = 'UNI' ) 
        
    def __unicode__(self): 
        return self.IntCode

    def LoadSampleData(self,number):
        x=0
        while (x<number):
            s = Sku( IntCode = "COD" + str(x),   MovUnit = 'UNI' )
            s.save()
            x=x+1
	

class SkuNames(models.Model): 
    """
	base clase for SKu Names 
    """
    Sku = models.ForeignKey(Sku) 
    Desc = models.CharField(max_length=200) 
    ShortDesc = models.CharField(max_length=40) 
    Lang = models.CharField(max_length=5, default = 'en-us' ) 

    def __unicode__(self): 
        return self.Desc

    def LoadSampleData(self,number):
        x=0
        while (x<number):
            s = Sku( IntCode = "COD" + str(x),   MovUnit = 'UNI' )
            s.save()
            x=x+1


class Barcode(models.Model): 
    """
	base clase for Bar codes  ( ) 
    """
    BarCode = models.CharField(max_length=13) 
    Sku = models.ForeignKey(Sku) 
    Multiplier = models.PositiveIntegerField( default = 1) 
        
    def __unicode__(self): 
        return self.BarCode 

    def LoadSampleData(self,number):
        x=0
        while (x<number):
            l = Sku.objects.get(IntCode =  "COD" + str(x))
            s = Barcode( Sku= l ,   BarCode = "560" + str(x), Multiplier = 1 )
            s.save()
            x=x+1
