from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.IntegerField()
    # quantity = models.IntegerField()
    
    # La fecha de creacion se puede cambiar 
    # created_at = models.DateField(auto_created=True)
    
    # La fecha actual se pone en automatico y no se puede cambiar
    created_at = models.DateField(auto_now_add=True)
    
