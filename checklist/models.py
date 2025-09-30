from django.contrib.auth.models import User
from django.db import models
from vehicle.models import Vehicle

class Checklists(models.Model):
  vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="checklists");
  driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="checklists");
  date = models.DateTimeField(verbose_name="Data")
  tires_ok = models.BooleanField(
    default=True,
    verbose_name="Pneus",
  )
  lights_ok = models.BooleanField(
    default=True,
    verbose_name="Luzes",
  )
  brakes_ok = models.BooleanField(
    default=True,
    verbose_name="Freios",
  )
  body_ok = models.BooleanField(
    default=True,
    verbose_name="Lataria",
  )
  notes = models.TextField(blank=True, null=True, verbose_name="Observações")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ["date"]
    verbose_name = "Vistoria"
    verbose_name_plural = "Vistorias"

  def __str__(self):
    return f"Checklist de {self.vehicle.plate_number} por {self.driver.username} em {self.date}"