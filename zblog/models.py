from django.db import models

class EntryQuerySet(models.QuerySet):
    def publicado(self):
        return self.filter(publico=True)

class Entrada (models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    publico = models.BooleanField(default=True)
    creado = models.DateField(auto_now_add=True)
    modificado = models.DateField(auto_now=True)

    objects = EntryQuerySet.as_manager()

    def __str__(self):
        return self.titulo