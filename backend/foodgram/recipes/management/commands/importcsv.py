import csv
import json

from django.core.management.base import BaseCommand

from recipes.models import Ingredient


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('../../data/ingredients.csv', encoding='utf-8', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                ingred, measure = row
                Ingredient.objects.create(
                    name=ingred,
                    measurement_unit=measure,
                )

# with open('ingredients.json', encoding='utf-8', mode='r') as file:
#     reader = json.dumps(file.readline())
#     print(reader)
