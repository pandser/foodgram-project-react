# Generated by Django 4.2.1 on 2023-05-23 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_alter_ingredientsinrecipes_amount_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='ingredients',
            new_name='ingredient',
        ),
    ]