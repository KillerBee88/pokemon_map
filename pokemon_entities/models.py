from django.db import models  # noqa F401

class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    title_en = models.CharField(max_length=200, blank=True, null=True, verbose_name='Название на английском')
    title_jp = models.CharField(max_length=200, blank=True, null=True, verbose_name='Название на японском')
    image = models.ImageField(upload_to='media', verbose_name='Изображение')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    previous_evolution = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='next_evolutions', 
        verbose_name='Эволюционирует из'
    )
    
    def __str__(self):
        return self.title

class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,
        related_name='entities', 
        verbose_name='Покемон'
    )
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(null=True, blank=True, verbose_name='Время появления')
    disappeared_at = models.DateTimeField(null=True, blank=True, verbose_name='Время исчезновения')
    level = models.IntegerField(verbose_name='Уровень')
    health = models.IntegerField(null=True, verbose_name='Здоровье')
    attack = models.IntegerField(null=True, verbose_name='Атака')
    defense = models.IntegerField(null=True, verbose_name='Защита')
    stamina = models.IntegerField(null=True, verbose_name='Выносливость')

    def __str__(self):
        return f"{self.pokemon.title} - {self.latitude}, {self.longitude}"
