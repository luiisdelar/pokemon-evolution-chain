from django.db import models
from django.db.models.base import Model

# Create your models here.


class Pokemon(models.Model):
    iid = models.IntegerField()
    name = models.CharField(max_length=200)
    height = models.IntegerField()
    weight = models.IntegerField()
    stats = models.ForeignKey(
        'Stats',
        on_delete=models.SET_NULL,
        null=True
    )
    evolution_chain = models.ForeignKey(
        'EvolutionChain', 
        null=True, 
        on_delete=models.SET_NULL, 
        related_name='evolution_chain'
    )


class Stats(models.Model):
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    special_attack = models.IntegerField()
    special_defense = models.IntegerField()
    speed = models.IntegerField()
    
    
class EvolutionChain(models.Model):
    min_level = models.IntegerField()
    evols_to = models.ForeignKey(
        'Pokemon', 
        null=True, 
        on_delete=models.CASCADE, 
        related_name='evols_to'
    )
    prevols_to = models.ForeignKey(
        'Pokemon', 
        null=True, 
        on_delete=models.CASCADE, 
        related_name='prevols_to'
    )

