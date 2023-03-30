from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class categoria(models.Model):
    nombre= models.CharField(max_length=50) 
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name='categoria'
       

    def __str__(self):
        return self.nombre
    

    
class post(models.Model):
    titulo= models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='blog', null=True, blank=True)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    categorias=models.ManyToManyField(categoria)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)
   


    class Meta:
        verbose_name='post'
       

    def __str__(self):
        return self.titulo