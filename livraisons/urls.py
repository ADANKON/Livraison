from django.urls import path
from .views import DemandeCreateView, DemandeListView, OffreCreateView, OffreListView

urlpatterns = [
    path('demandes/', DemandeListView.as_view(), name='list-demande'),
    path('demandes/nouvelle/', DemandeCreateView.as_view(), name='creer-demande'),
    path('offres/', OffreCreateView.as_view(), name='creer-offre'),
    path('offres/<int:demande_id>/', OffreListView.as_view(), name='offres-par-demande'),
]