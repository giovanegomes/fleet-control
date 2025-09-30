from django.contrib.auth.models import User
from django.db import models
from vehicle.models import Vehicle

class Trips(models.Model):
  vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="trips");
  driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="trips");
  start_odometer = models.IntegerField(verbose_name="Odômetro inicial")
  end_odometer = models.IntegerField(verbose_name="Odômetro final")
  start_location = models.CharField(verbose_name="Local de partida", max_length=255)
  end_location = models.CharField(verbose_name="Local de destino", max_length=255)
  purpose = models.CharField(verbose_name="Motivo da viagem", max_length=255)
  start_time = models.DateTimeField(auto_now_add=True)
  end_time = models.DateTimeField(auto_now=True)
  notes = models.TextField(blank=True, null=True, verbose_name="Observações")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ["-start_time"]
    verbose_name = "Viagem"
    verbose_name_plural = "Viagens"

  def __str__(self):
    return f"Viagem de {self.vehicle.plate_number} por {self.driver.username} em {self.start_time}"
