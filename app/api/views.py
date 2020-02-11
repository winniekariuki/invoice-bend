import csv
import os
import itertools
import calendar
import datetime
from django.db import connection
from django.conf import settings
from rest_framework import mixins, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework import status

from .serializers import CSVParserSerializer
from .helpers import format_date
from .models import CSVParser

customer_total_amt_sql = '''
select contact_name, due_date, (quantity*unit_amount) as Total from (select invoice_date, quantity, unit_amount,
due_date, contact_name FROM api_csvparser ORDER BY invoice_date) as sample order by Total desc'''

top_customer_quantity_sql = '''select contact_name, quantity FROM api_csvparser order by quantity desc'''


class CSVParseAPIView(generics.CreateAPIView):

    serializer_class = CSVParserSerializer

    def post(self, request, format=None):

        request_data = request.data.get("data")
        CSVParser.objects.all().delete()
        data = []
        for row in request_data:
            obj = {
                "contact_name": row['ContactName'],
                "invoice_number": row['InvoiceNumber'],
                "invoice_date": format_date(row['InvoiceDate']),
                "due_date": format_date(row['DueDate']),
                "description": row['Description'],
                "quantity": row['Quantity'],
                "UnitAmount": row['UnitAmount'],
                "unit_amount": row['UnitAmount'],
            }
            data.append(obj)
            serializer = self.serializer_class(data=obj)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        data = CSVParser.objects.all()
        serializer = self.serializer_class(data, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MonthlyTotalAPIView(generics.ListAPIView):

    serializer_class = CSVParserSerializer

    def get(self, request):
        instance = CSVParser.objects.all()
        data = {}
        for each in instance:

            year = each.invoice_date.year
            month = calendar.month_name[each.invoice_date.month]
            total = each.unit_amount*each.quantity

            obj = {year: {month: total}}
            try:
                year_data = data[year]
                try:
                    month_total = year_data[month]
                    year_data.update({month: month_total+total})
                except:
                    year_data.update(obj[year])

            except:
                data.update(obj)
        month_defaults = ['January', 'February', 'March', 'April', 'May', 'June',
                          'July', 'August', 'September', 'October', 'November', 'December']
        for year in data:
            months = ([*data[year]])

            unavailable = [m for m in month_defaults if m not in months]

            for each in unavailable:
                data[year].update({each: 0})
        return Response(data, status=status.HTTP_200_OK)


class TopCustomersAPIView(generics.ListAPIView):

    serializer_class = CSVParserSerializer

    def get(self, request):
        cursor = connection.cursor()
        cursor.execute(customer_total_amt_sql)
        instance = cursor.fetchall()
        data = {}
        for each in instance:
            customer, year, total = each
            year = year.year

            obj = {year: {customer: total}}
            try:
                year_data = data[year]
                try:
                    customer_total = year_data[customer]
                    year_data.update({customer: customer_total+total})
                except:
                    year_data.update(obj[year])

            except:
                data.update(obj)
        final = {}
        for year in data:
            sorted_data = {k: v for k, v in sorted(
                data[year].items(),
                key=lambda item: item[1], reverse=True)}
            slice_year = dict(itertools.islice(sorted_data.items(), 5))
            final.update({year: slice_year})

        return Response(final, status=status.HTTP_200_OK)


class TopCustomersQuantityAPIView(generics.ListAPIView):

    serializer_class = CSVParserSerializer

    def get(self, request):
        cursor = connection.cursor()
        cursor.execute(top_customer_quantity_sql)
        instance = cursor.fetchall()
        data = {}
        for each in instance:
            customer, total = each
            obj = {customer: total}
            data.update(obj)
        sorted_data = {k: v for k, v in sorted(
            data.items(),
            key=lambda item: item[1], reverse=True)}
        slice_year = dict(itertools.islice(sorted_data.items(), 5))

        return Response(slice_year, status=status.HTTP_200_OK)


class InvoiceAPIView(generics.ListAPIView):

    serializer_class = CSVParserSerializer

    def get(self, request):
        date = request.query_params['date']
        date = format_date(date)
        next_date = date + datetime.timedelta(30)
        instance = CSVParser.objects.filter(invoice_date__range=[date, next_date]).only(
            "invoice_date", "quantity", "unit_amount")
        data = []
        for each in instance:
            total = each.unit_amount * each.quantity

            obj = {"total": total, "invoice_date": each.invoice_date}
            if data:
                for i, item in enumerate(data):
                    if item['invoice_date'] == obj['invoice_date']:
                        obj["total"] += item['total']
                        data[i] = obj
            data.append(obj)
        return Response(data, status=status.HTTP_200_OK)
