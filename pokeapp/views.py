from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
import requests
from pokeapp.models import EvolsTo, Pokemon

# Create your views here.

def index(request, search):
    json = {}
    
    pokemons = Pokemon.objects.filter(name__icontains=search)
    for po in pokemons:
        print(po.name)
    for pokemon in pokemons:
        index = f'pokemon-{pokemon.iid}'
        json[index] = ({ 
            "id": pokemon.iid,
            "name": pokemon.name, 
            "height": pokemon.height,
            "weight": pokemon.weight,
            "hp": pokemon.stats.hp,
            "attack": pokemon.stats.attack,
            "defense": pokemon.stats.defense,
            "special_attack": pokemon.stats.special_attack,
            "special_defense": pokemon.stats.special_defense,
            "speed": pokemon.stats.speed
        })
        
        evolution1 = pokemon.evolution_chain.evolutions
        evolution2 = evolution1.evols_to
        
        #print(pokemon.evolsto.evols_to.pokemon.name)
        #json[index]["evolution_type"] = pokemon.evolsto.pokemon.name
        
        if evolution2.evols_to:
            return HttpResponse(f'{evolution1.pokemon.name} -> {evolution2.pokemon.name} -> {evolution2.evols_to.pokemon.name}')
        else:
            return HttpResponse(f'{evolution1.pokemon.name} -> {evolution2.pokemon.name} ')
    #print(json)
    #    return render(request, "index.html", {'pokemon': pokemon})
    
    #return HttpResponse("Nada")
        