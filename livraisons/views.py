from django.shortcuts import render
from rest_framework import generics, permissions
from .models import DemandeLivraison, OffreLivraison
from .serializers import DemandeLivraisonSerialiser, OffreLivraisonSerializer

#creer une demande de livraison
class DemandeCreateView(generics.CreateAPIView):
    serializer_class = DemandeLivraisonSerialiser
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.seve(client=self.request.user)


#creer une offre de livraison
class OffreCreateView(generics.CreateAPIView):
    serializer_class = OffreLivraisonSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.seve(livreur=self.request.user)


#voir la liste des demandes disponibles
class DemandeListView(generics.ListAPIView):
    queryset = DemandeLivraison.objects.filter(statut='en_attente')
    serializer_class = DemandeLivraisonSerialiser
    permission_classes = [permissions.IsAuthenticated]


#liste des offres faite sur une demande
class OffreListView(generics.ListAPIView):
    serializer_class = OffreLivraisonSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        demande_id = self.kwargs['demande_id']
        return OffreLivraison.objects.filter(demande_id=demande_id)