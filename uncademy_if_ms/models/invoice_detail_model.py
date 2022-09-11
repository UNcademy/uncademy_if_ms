from django.db import models

class InvoiceDetail(models.Model):
    
    id = models.AutoField(primary_key = True)
    t_payment_value = models.FloatField()
    t_payment_date = models.DateField()
    ut_payment_value =  models.FloatField()
    ut_payment_date = models.DateField()
    reason = models.CharField(max_length=200)

    class Meta:
        app_label = 'uncademy_if_ms'
