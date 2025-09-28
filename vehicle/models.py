from django.db import models

class Vehicle(models.Model):
  class FuelType(models.TextChoices):
    GASOLINE = "GAS", "Gasolina"
    DIESEL = "DSL", "Diesel"
    ETHANOL = "ETH", "Etanol"
    ELECTRIC = "ELE", "Eléctrico"
    HYBRID = "HYB", "Híbrido"

  plate_number = models.CharField(
    max_length=10,
    unique=True,
    verbose_name="Placa",
  )
  brand = models.CharField(max_length=50, verbose_name="Marca")
  model = models.CharField(max_length=50, verbose_name="Modelo")
  year = models.PositiveIntegerField(verbose_name="Ano")
  mileage = models.PositiveIntegerField(
    default=0,
    verbose_name="Quilometragem"
  )
  fuel_type = models.CharField(
    max_length=3,
    choices=FuelType.choices,
    default=FuelType.GASOLINE,
    verbose_name="Tipo de combustível"
  )
  is_active = models.BooleanField(
    default=True,
    verbose_name="Ativo",
  )
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ["brand", "model", "year"]
    verbose_name = "Veículo"
    verbose_name_plural = "Veículos"

  def __str__(self):
    return f"{self.brand} {self.model} ({self.plate_number})"