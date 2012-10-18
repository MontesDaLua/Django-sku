from django.db import models

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
    Desc = models.CharField(max_length=200) 
    ShortDesc = models.CharField(max_length=40) 
        
    def __unicode__(self): 
        return self.IntCode

