import csv

from django.core.management.base import BaseCommand

from recipes.models import Ingredient


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('static/ingredients.csv',
                  encoding='utf-8', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                ingred, measure = row
                Ingredient.objects.create(
                    name=ingred,
                    measurement_unit=measure,
                )
