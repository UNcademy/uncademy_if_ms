from django.db import models
from .invoice_detail_model import InvoiceDetail

class Invoice(models.Model):

    id = models.AutoField(primary_key = True)
    user_id = models.UUIDField()
    invoice_detail = models.ForeignKey(InvoiceDetail, on_delete = models.CASCADE)
    payment_date = models.DateField()
    is_payed = models.BooleanField() 

    class Meta:
        app_label = 'uncademy_if_ms'
