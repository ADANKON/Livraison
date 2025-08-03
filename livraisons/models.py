from django.db import models
from users.models import User

# Create your models here.

class DemandeLivraison(models.Model):
    STATUT_CHOICES = [
        ('en_attente', 'En_attente'),
        ('acceptee', 'Acceptee'),
        ('en_cours', 'En_cours'),
        ('livree', 'Livree'),
        ('annulee', 'Annulee'),      
        ]
    
    client = models.ForeignKey(User,on_delete=models.CASCADE,related_name='demandes')
    titre = models.CharField(max_length=255)
    description = models.TextField()
    adresse_depart = models.CharField(max_length=255)
    adresse_arrivee = models.CharField(max_length=255)
    date_livraison =  models.DateField()
    statut = models.CharField(max_length=20,choices=STATUT_CHOICES)
    date_creaton = models.DateField(auto_now_add=True)


    def __str__(self):
        return f"{self.titre} ({self.statut})"


class OffreLivraison(models.Model):
    livreur = models.ForeignKey(User,on_delete=models.CASCADE,related_name='offres')
    demande = models.ForeignKey(DemandeLivraison,on_delete=models.CASCADE,related_name='offres')
    prix_propose = models.DecimalField(max_digits=10,decimal_places=2)
    est_acceptee = models.BooleanField(default=False)
    date_offres = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Offre de {self.livreur.email} pour {self.demande.titre}"
