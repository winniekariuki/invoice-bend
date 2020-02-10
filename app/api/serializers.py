from rest_framework import serializers
from django.conf import settings
import calendar
from .models import CSVParser


class CSVParserSerializer(serializers.ModelSerializer):

    invoice_number = serializers.IntegerField(required=True)
    contact_name = serializers.CharField(required=True)
    invoice_date = serializers.DateField(required=True)
    due_date = serializers.DateField(required=True)
    description = serializers.CharField(required=True)
    quantity = serializers.IntegerField(required=True)
    unit_amount = serializers.IntegerField(required=True)

    class Meta:
        model = CSVParser
        fields = '__all__'
