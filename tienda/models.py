from django.db import models

# Create your models here.

class categoriaProd(models.Model):
    nombre=models.CharField(max_length=70)
    created=models.DateField(auto_now=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="categoriaProd"
        

    def __str__(self):
        return self.nombre
    

class producto(models.Model):
    nombre=models.CharField(max_length=70)
    categorias=models.ForeignKey(categoriaProd, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="tienda", null=True, blank=True)
    precio=models.FloatField()
    disponibilidad=models.BooleanField(default=True)
    created=models.DateField(auto_now=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:

        verbose_name="producto"
        
