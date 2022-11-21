from django.db import models
from django.urls import reverse

from django.utils.translation import gettext as _

# Create your models here.


class Benson(models.Model):
    id = models.BigAutoField(primary_key=True, serialize=False)
    part_number = models.TextField(_("Part Number"), blank=True, null=True)
    product = models.TextField(_("PRODUCT"), blank=True, null=True)
    color = models.TextField(_("COLOR"), blank=True, null=True)
    vehicle = models.TextField(_("VEHICLE"), blank=True, null=True)

    def __str__(self):
        return f"{self.part_number}: {self.product} - {self.color}"