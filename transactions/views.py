from django.shortcuts import render
from .serializers import PortefeuilleSerializer, TransactionSerializer
from rest_framework import generics, permissions,status
from .models import Portefeuille, Transaction
from rest_framework.response import Response

#Afficher le portefeuille de l'utilisateur
class MonPortefeuilleView(generics.RetrieveAPIView):
    serializer_class = PortefeuilleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        portefeuille,_ = Portefeuille.objects.get_or_create(user=self.request.user)
        return portefeuille


#Faire une recharge manuelle
class RechargeView(generics.CreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        portefeuille, _ = Portefeuille.objects.get_or_create(user=self.request.user)
        montant = serializer.validated_data['montant']
        portefeuille.solde += montant
        portefeuille.seve()
        
        serializer.seve(portefeuille=portefeuille, type='recharge', description='Recharge manuelle')


#Historique des transactions
class MesTransactionsView(generics.ListAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        portefeuille, _ = Portefeuille.objects.get_or_create(user=self.request.user)
        return portefeuille.transactions.all().order_by('-date')
    
    