from django.db import models
from django.contrib import admin

class Lote(models.Model):
    identificador = models.CharField(max_length=100)
    fecha = models.DateField(auto_now_add=True)

@admin.register(Lote)
class LoteAdmin(admin.ModelAdmin):
    pass