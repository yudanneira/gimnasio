from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


# Create your models here.

class Photo (models.Model):
	
	nombre = models.CharField(max_length=20)
	photo = models.ImageField(upload_to='photos/')

	def __str__(self):
		return '{}'.format(self.photo)


class Grupomuscular (models.Model):
	nombre = models.CharField(max_length=20)
	descripcion = models.CharField(max_length=200)
	photo = models.ForeignKey(Photo, null=True, blank=True)

	def __str__(self):
		return '{}'.format(self.nombre)

@receiver(post_delete, sender=Photo)
def photo_delete(sender, instance, **kwargs):
    """ Borra los ficheros de las fotos que se eliminan. """
    instance.photo.delete(False)
