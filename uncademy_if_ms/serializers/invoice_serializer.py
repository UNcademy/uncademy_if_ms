from rest_framework import serializers
from uncademy_if_ms.models.invoice_model import Invoice
from uncademy_if_ms.models.invoice_detail_model import InvoiceDetail
from uncademy_if_ms.serializers.invoice_detail_serializer import InvoiceDetailSerializer

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Invoice
        fields = ['id', 'user_id', 'invoice_detail', 'payment_date', 'is_payed']

    def create(self, validated_data):
        invoice = Invoice(id = validated_data.get("id"),
                            user_id = validated_data.get("user_id"),
                            invoice_detail = validated_data.get("invoice_detail"),
                            payment_date = validated_data.get("payment_date"),
                            is_payed = validated_data.get("is_payed"))
        invoice.save()
        return invoice
        
    def update(self, instance, validated_data):
        instance.id = validated_data.get("id")
        instance.user_id = validated_data.get("user_id")
        instance.invoice_detail = validated_data.get("invoice_detail")
        instance.payment_date = validated_data.get("payment_date")
        instance.is_payed = validated_data.get("is_payed")
        instance.save()
        return instance

    def to_representation(self, obj):
        data = super().to_representation(obj)
        invoiceDetail = InvoiceDetail.objects.get(id = data["invoice_detail"])
        invoiceDetailSerializer = InvoiceDetailSerializer(invoiceDetail)
        data["invoice_detail"] = invoiceDetailSerializer.data 
        return data
