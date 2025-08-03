from rest_framework import serializers
from .models import Portefeuille, Transaction

class PortefeuilleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portefeuille
        fields = ['id', 'user', 'solde']
        read_only_fields = ['user', 'solde']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
        read_only_field = ['portefeuille', 'date']
        
