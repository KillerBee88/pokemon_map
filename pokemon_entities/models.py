from django.db import models  # noqa F401

class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True, upload_to='media')
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return '{}'.format(self.title)

class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,
        related_name='entities'
    )
    latitude = models.FloatField()
    longitude = models.FloatField()
    appeared_at = models.DateTimeField(null=True, blank=True)
    disappeared_at = models.DateTimeField(null=True, blank=True)
    level = models.IntegerField(default=0)
    health = models.IntegerField(default=0)
    attack = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)
    stamina = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.pokemon.title} - {self.latitude}, {self.longitude}"
