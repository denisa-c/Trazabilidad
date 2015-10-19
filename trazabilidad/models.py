from django.db import models
from django.utils.encoding import force_bytes
from django.contrib import admin


class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_creacion = models.DateField(auto_now_add=True)
    ingredientes = models.ManyToManyField('Ingrediente')

    def __unicode__(self):
        return force_bytes('%s (%s)' % (self.nombre, self.fecha_creacion))


class Lote(models.Model):
    identificador = models.CharField(max_length=100)
    producto = models.ForeignKey(Producto)
    fecha_fabricacion = models.DateField(auto_now_add=True)
    cantidad = models.FloatField()

    def __unicode__(self):
        return force_bytes('%s' % self.identificador)


class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100)
    lote = models.CharField(max_length=20)
    marca = models.CharField(max_length=100)

    def __unicode__(self):
        return force_bytes('%s - %s' % (self.nombre, self.marca))


class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    nif = models.CharField(max_length=30)

    def __unicode__(self):
        return force_bytes('%s' % self.nombre)


class Venta(models.Model):
    cliente = models.ForeignKey(Cliente)
    lote = models.ForeignKey(Lote)
    fecha_venta = models.DateField(auto_now_add=True)
    cantidad = models.FloatField()

    def __unicode__(self):
        return force_bytes('%s | %s | %s' % (self.lote, self.fecha_venta, self.cliente))


class Empresa(models.Model):
    nombre = models.CharField(max_length=100)
    logotipo = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    cif = models.CharField(max_length=30)
    nrs = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    web = models.CharField(max_length=50)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    pass


@admin.register(Lote)
class LoteAdmin(admin.ModelAdmin):
    pass


@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    pass


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    pass


@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    pass


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    pass
