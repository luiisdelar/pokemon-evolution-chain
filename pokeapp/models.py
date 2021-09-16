from django.db import models
from django.db.models.base import Model

# Create your models here.


class Pokemon(models.Model):
    iid = models.IntegerField()
    name = models.CharField(max_length=200)
    height = models.IntegerField()
    weight = models.IntegerField()
    stats = models.OneToOneField(
        'Stats',
        on_delete = models.SET_NULL,
        null = True
    )
    evolution_chain = models.OneToOneField(
        'EvolutionChain', 
        null = True, 
        on_delete = models.SET_NULL, 
    #    related_name = 'evolution_chain'
    )


class EvolutionChain(models.Model):    
    evolutions = models.OneToOneField(
        'EvolsTo',  
        on_delete = models.CASCADE,
        null = True, 
    #    related_name = 'evolutions'
    )
    

class EvolsTo(models.Model):
    pokemon = models.OneToOneField(
        'Pokemon', 
        null = True, 
        on_delete = models.CASCADE, 
    #    related_name = 'pokemon'
    )
    evols_to = models.OneToOneField(
        'self',
        null = True,
        on_delete = models.CASCADE, 
        #related_name = 'evols_to'
    )


class Stats(models.Model):
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    special_attack = models.IntegerField()
    special_defense = models.IntegerField()
    speed = models.IntegerField()