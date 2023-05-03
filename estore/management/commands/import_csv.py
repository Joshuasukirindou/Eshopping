import csv
from decimal import Decimal
import decimal
from django.shortcuts import render
from pathlib import Path
from django.db import models
from django.core.management.base import BaseCommand, CommandError
from estore.models import Product


class Command(BaseCommand):
    help = 'Load data from csv'

    def handle(self, *args, **options):
        # drop the data from the table so that if we rerun the file, we don't repeat values
        Product.objects.all().delete()
        print("table dropped successfully")

        # create table again

        # open the file to read it into the database
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        with open(str(base_dir) + '/estore/static/csv/Product_range.csv', newline='') as f:
            reader = csv.reader(f, delimiter=",")
            next(reader) # skip the header line
            for row in reader:
                print(row)
                try:
                    product = Product.objects.create(
                        product_id=int(row[0]),
                        name=row[2],
                        price=int(float(row[3])) if row[3] else 0,
                        country=row[5],
                        size=Decimal(row[6]) if row[6] else Decimal('0'),
                        ABV=Decimal(row[7]) if row[7] else Decimal('0'),
                    )
                except decimal.InvalidOperation:
                    print(f"Failed to convert {row[6]} or {row[7]} to Decimal")
                    continue

                product.save()

                print("data import successfully")


