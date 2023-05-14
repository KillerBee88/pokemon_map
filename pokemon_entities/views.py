import folium
import json

from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.utils import timezone
from .models import PokemonEntity, Pokemon


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    current_time = timezone.localtime()
    pokemons = Pokemon.objects.all()
    active_pokemons = PokemonEntity.objects.filter(
        appeared_at__lte=current_time,
        disappeared_at__gt=current_time,
    )

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in active_pokemons:
        add_pokemon(
            folium_map, pokemon_entity.latitude,
            pokemon_entity.longitude,
            request.build_absolute_uri(pokemon_entity.pokemon.image.url) if pokemon_entity.pokemon.image else DEFAULT_IMAGE_URL
        )

    pokemons_on_page = []
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': request.build_absolute_uri(pokemon.image.url) if pokemon.image else DEFAULT_IMAGE_URL,
            'title_ru': pokemon.title,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    try:
        requested_pokemon = Pokemon.objects.get(id=pokemon_id)
    except Pokemon.DoesNotExist:
        return HttpResponseNotFound('<h1>Такой покемон не найден</h1>')

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    pokemon_entities = PokemonEntity.objects.filter(pokemon=requested_pokemon)
    for pokemon_entity in pokemon_entities:
        add_pokemon(
            folium_map, pokemon_entity.latitude,
            pokemon_entity.longitude,
            request.build_absolute_uri(pokemon_entity.pokemon.image.url) if pokemon_entity.pokemon.image else DEFAULT_IMAGE_URL
        )

    evolution_from = None
    if requested_pokemon.evolution_from:
        evolution_from = {
            "title_ru": requested_pokemon.evolution_from.title,
            "pokemon_id": requested_pokemon.evolution_from.id,
            "img_url": request.build_absolute_uri(requested_pokemon.evolution_from.image.url) if requested_pokemon.evolution_from.image else DEFAULT_IMAGE_URL,
        }

    next_evolution = None
    next_evolution_objs = requested_pokemon.evolutions.all()
    if next_evolution_objs:
        next_evolution_obj = next_evolution_objs[0]
        next_evolution = {
            "title_ru": next_evolution_obj.title,
            "pokemon_id": next_evolution_obj.id,
            "img_url": request.build_absolute_uri(next_evolution_obj.image.url) if next_evolution_obj.image else DEFAULT_IMAGE_URL,
        }

    pokemon = {
        'pokemon_id': requested_pokemon.id,
        'img_url': request.build_absolute_uri(requested_pokemon.image.url) if requested_pokemon.image else DEFAULT_IMAGE_URL,
        'title_ru': requested_pokemon.title,
        'title_en': requested_pokemon.title_en,
        'title_jp': requested_pokemon.title_jp,
        'description': requested_pokemon.description,
        'previous_evolution': evolution_from,
        'next_evolution': next_evolution,
    }

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 
        'pokemon': pokemon
    })
