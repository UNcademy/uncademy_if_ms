from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from uncademy_if_ms.views.invoice_detail_view import InvoiceDetailDetail
from uncademy_if_ms.views.invoice_detail_view import InvoiceDetailList
from uncademy_if_ms.views.invoice_view import InvoiceList, InvoiceinDetail


urlpatterns = [
    path('invoice-details/', InvoiceDetailList.as_view()),
    path('invoice-details/<int:pk>', InvoiceDetailDetail.as_view()),
    path('invoice/', InvoiceList.as_view()),
    path('invoice/<user_id>', InvoiceList.as_view()),
    path('invoice/<int:pk>', InvoiceinDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)