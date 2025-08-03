from django.urls import path
from .views import MonPortefeuilleView, MesTransactionsView, RechargeView

urlpatterns = [
    path('me/', MonPortefeuilleView.as_view(), name='mon-portefeuille'),
    path('recharge/', RechargeView.as_view(), name='recharge'),
    path('historique/', MesTransactionsView.as_view(), name='historique'),
]