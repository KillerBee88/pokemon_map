# Generated by Django 4.2.1 on 2023-05-14 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='previous_evolutions',
            new_name='evolution_from',
        ),
    ]
