from django.db import models

# Create your models here.

class Note(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    alert = models.DateTimeField()
    
    price = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'Nota: {self.name} | Fecha: {self.alert}'