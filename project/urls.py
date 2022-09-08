from django.urls import path, include

urlpatterns = [
    path('', include('sia_if_ms.urls')),
]

