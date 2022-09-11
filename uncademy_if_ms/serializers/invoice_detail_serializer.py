from rest_framework import serializers
from uncademy_if_ms.models.invoice_detail_model import InvoiceDetail

class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = ['id', 't_payment_value', 't_payment_date', 'ut_payment_value', 'ut_payment_date', 'reason']

    def create(self, validated_data):
        invoice_detail = InvoiceDetail(t_payment_value = validated_data.get("t_payment_value"),
                                        t_payment_date = validated_data.get("t_payment_date"),
                                        ut_payment_value = validated_data.get("ut_payment_value"),
                                        ut_payment_date = validated_data.get("ut_payment_date"),
                                        reason = validated_data.get("reason"))
        invoice_detail.save()
        return invoice_detail

    def update(self, instance, validated_data):
        instance.t_payment_value = validated_data.get("t_payment_value")
        instance.t_payment_date = validated_data.get("t_payment_date")
        instance.ut_payment_value = validated_data.get("ut_payment_value")
        instance.ut_payment_date = validated_data.get("ut_payment_date")
        instance.reason = validated_data.get("reason")
        instance.save()
        return instance

    def to_representation(self, obj):
        data = super().to_representation(obj)
        return data
