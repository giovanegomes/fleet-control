from django.contrib.auth.models import User
from django.db import models
from vehicle.models import Vehicle

class FuelLogs(models.Model):
  vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="fuel_logs");
  driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="fuel_logs");
  date = models.DateTimeField(verbose_name="Data")
  odometer = models.IntegerField(verbose_name="Odômetro")
  liters = models.DecimalField(verbose_name="Litros", max_digits=7, decimal_places=2)
  total_value = models.DecimalField(verbose_name="Valor total", max_digits=7, decimal_places=2)
  station_name = models.CharField(verbose_name="Posto", max_length=255, blank=True, null=True)
  receipt_photo_url = models.TextField(verbose_name="receipt_photo_url", blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ["-date"]
    verbose_name = "Abastecimento"
    verbose_name_plural = "Abastecimentos"

  def __str__(self):
    return f"Abastecimento de {self.vehicle.plate_number} por {self.driver.username} em {self.date}"
