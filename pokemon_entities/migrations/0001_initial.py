# Generated by Django 4.2.1 on 2023-05-14 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('title_en', models.CharField(blank=True, max_length=200, null=True)),
                ('title_jp', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media')),
                ('description', models.TextField(blank=True, null=True)),
                ('previous_evolutions', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='evolutions', to='pokemon_entities.pokemon')),
            ],
        ),
        migrations.CreateModel(
            name='PokemonEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('appeared_at', models.DateTimeField(blank=True, null=True)),
                ('disappeared_at', models.DateTimeField(blank=True, null=True)),
                ('level', models.IntegerField(default=0)),
                ('health', models.IntegerField(default=0)),
                ('attack', models.IntegerField(default=0)),
                ('defense', models.IntegerField(default=0)),
                ('stamina', models.IntegerField(default=0)),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entities', to='pokemon_entities.pokemon')),
            ],
        ),
    ]
