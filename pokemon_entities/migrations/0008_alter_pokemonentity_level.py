# Generated by Django 4.2.1 on 2023-05-15 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0007_alter_pokemon_previous_evolution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='level',
            field=models.IntegerField(verbose_name='Уровень'),
        ),
    ]