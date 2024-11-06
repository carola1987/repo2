from django.db import models

# Create your models here.
class flan(models.Model):
    flan_uuid = models.UUIDField()
    nombre = models.CharField(max_length=64)
    descripcion = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField()
    is_private = models.BooleanField()

def __str__(self):
        return self.nombre