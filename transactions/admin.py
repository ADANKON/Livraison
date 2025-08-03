from django.contrib import admin
from .models import Portefeuille, Transaction
# Register your models here.

admin.site.register(Portefeuille)
admin.site.register(Transaction)