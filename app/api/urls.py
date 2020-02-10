from django.urls import path

from .views import (CSVParseAPIView, MonthlyTotalAPIView, TopCustomersAPIView,
                    TopCustomersQuantityAPIView, InvoiceAPIView)

urlpatterns = [
    path('upload', CSVParseAPIView.as_view(), name="upload-csv"),
    path('monthly-total', MonthlyTotalAPIView.as_view(), name="monthly-total"),
    path('top-customers-amount', TopCustomersAPIView.as_view(),
         name="top-customers-amount"),
    path('top-customers-quantity', TopCustomersQuantityAPIView.as_view(),
         name="top-customers-quantity"),
    path('invoice', InvoiceAPIView.as_view(),
         name="invoice"),
]
