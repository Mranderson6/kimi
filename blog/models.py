from datetime import timezone
import os
from django.db import models
from django.urls import reverse

from user.models import CustomUser

# Create your models here.
def categorieImage(instance, filename):
    upload_to = 'media/_image/'
    ext = filename.split('.')[-1]
    # recuperation du nom de l'image
    if instance.nom:
        filename = '{}.{}'.format(instance.nom, ext)
        return os.path.join(upload_to, filename)


class Categorie(models.Model):
    nom = models.CharField(max_length=250)
    image = models.ImageField(upload_to=categorieImage)
    couleur = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.nom
    
    def get_absolute_url(self):
        return reverse("blog:categorieDetails", kwargs={"id": self.id})
    


class BlogPost(models.Model):
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now= True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog:detail-post", kwargs={"id": self.id})
    
    
def _image(instance, filename):
    upload_to = 'media/_image/'
    ext = filename.split('.')[-1]
    # recuperation du nom de l'image
    if instance.nom:
        filename = '{}.{}'.format(instance.nom, ext)
        return os.path.join(upload_to, filename)
    
class itemImage(models.Model):
    nom = models.CharField(max_length=50)
    image = models.ImageField(upload_to=_image)
    item = models.ForeignKey(BlogPost, on_delete=models.CASCADE)


class newsletter (models.Model):
    mail = models.EmailField()

    def __str__(self):
        return self.mail
    
class blogComment(models.Model):
    nom = models.CharField(max_length=250)
    mail = models.EmailField()
    message = models.TextField()

    def __str__(self) -> str:
        return self.nom
    

class clientMessage(models.Model):
    nom = models.CharField(max_length=250)
    mail = models.EmailField()
    objet = models.CharField(max_length=250)
    message = models.TextField()

    def __str__(self):
        return self.nom