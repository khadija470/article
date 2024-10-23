from django.db import models
from django.contrib.auth.models import User
class Article(models.Model):
        titre= models.CharField(max_length= 150)
        resume= models.CharField(max_length= 250)
        contenu= models.TextField(blank=True)
        auteur= models.ForeignKey(User,on_delete=models.CASCADE)
        date_publication = models.DateField(auto_now_add=True)
        image = models.ImageField(upload_to='media/images/',blank=True,null=True)
        prix_kilo = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
        origine = models.CharField(max_length=100, null=True, blank=True)
        disponible = models.BooleanField(default=True, null=True, blank=True)
        quantite_disponible = models.DecimalField(max_digits=6, decimal_places=2, default=0, null=True, blank=True)
        mode_conservation = models.CharField(max_length=50, null=True, blank=True)
        temps_livraison = models.CharField(max_length=50, null=True, blank=True)
# Create your models here.
        def __str__(self):
            return f"{self.titre}"
