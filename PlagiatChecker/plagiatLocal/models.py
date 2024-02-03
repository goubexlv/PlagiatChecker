from django.db import models

class Document(models.Model):
    nomdoc = models.FileField(upload_to='public',null=True )
   
    class Meta:
        db_table = "document"      
        
        
    
class Documentverification(models.Model):
    nomdoc = models.FileField(upload_to='public',null=True)
    auteur = models.CharField(max_length=200)
   
    class Meta:
        db_table = "documentverification"  
        
        
class Rapport(models.Model):
    nomdoc = models.CharField(max_length=200)
    nomtest = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    ratio = models.IntegerField()
    idtest = models.IntegerField()
   
    class Meta:
        db_table = "rapport"
    

    
