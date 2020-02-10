from django.db import models
from django.utils import timezone

class CSVParser(models.Model):
    """
    CSVParser model
    """
    invoice_number = models.IntegerField(db_index=True, blank=False)
    contact_name = models.CharField(max_length=20, blank=False)
    invoice_date = models.DateField(blank=False, default=timezone.now)
    due_date = models.DateField(blank=False, default=timezone.now)
    description = models.CharField(blank=False, max_length=1000)
    quantity = models.IntegerField(db_index=True, blank=False)
    unit_amount = models.IntegerField(db_index=True, blank=False)
