from django.db import models
from users.models import User

class Portefeuille(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    solde = models.DecimalField(max_digits=13,decimal_places=2,default=0.0)

    def __str(self):
        return f"{self.user.email} - {self.solde}"


class Transaction(models.Model):
    TYPE_CHOICES = (
        ('recharge', 'Recharge'),
        ('paiement', 'Paiement'),
        ('retrait', 'Retrait'),
        ('remboursememt', 'Remboursement'),
    )

    portefeuille = models.ForeignKey(Portefeuille,on_delete=models.CASCADE,related_name='transaction')
    montant = models.DecimalField(max_digits=10,decimal_places=2)
    type = models.CharField(max_length=15, choices=TYPE_CHOICES)
    date = models.DateField(auto_now_add=True)
    description = models.TextField(blank=True)

    def __stt__(self):
        return f"{self.type} de {self.montant} effectuer dans le compe de {self.portefeuille.user.email}"