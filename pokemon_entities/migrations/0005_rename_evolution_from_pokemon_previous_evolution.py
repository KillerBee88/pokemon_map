# Generated by Django 4.2.1 on 2023-05-14 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0004_alter_pokemon_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='evolution_from',
            new_name='previous_evolution',
        ),
    ]
