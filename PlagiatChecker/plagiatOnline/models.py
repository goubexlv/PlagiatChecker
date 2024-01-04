from django.db import models
from django.db import models

class Documents(models.Model):
    file = models.FileField(upload_to='public',null=True)
   
    class Meta:
        db_table = "documents"      
        
