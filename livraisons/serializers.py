from rest_framework import serializers
from .models import DemandeLivraison, OffreLivraison

class DemandeLivraisonSerialiser(serializers.ModelSerializer):
    class Meta:
        model = DemandeLivraison
        fields = '__all__'
        read_only_fields = ['client', 'statu', 'date_creation']


class OffreLivraisonSerializer(serializers.ModelSerializer):
    class Meta:
        model = OffreLivraison
        fields = '__all__'
        read_only_fields = ['livreur', 'date_offre']