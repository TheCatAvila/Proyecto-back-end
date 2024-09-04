from django.db import models

# Create your models here.

class Categoria(models.Model):
    tipo = models.CharField(max_length=40)
    
    def __str__(self):
        return self.tipo
    
class Producto(models.Model):
    nombre      = models.CharField(max_length=20)
    description = models.CharField(max_length=250)
    precio      = models.IntegerField()
    
    tipo = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre