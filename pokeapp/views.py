from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
import requests
from pokeapp.models import EvolsTo, Pokemon

# Create your views here.

def index(request, search):
    json = {}
    
    pokemons = Pokemon.objects.filter(name__icontains=search)
    
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
       # print(pokemon.evolsto.evols_to.pokemon.name)
        #json[index]["evolution_type"] = pokemon.evolsto.pokemon.name
        break
        #print(pokemon.name) 

    print(json)
    #    return render(request, "index.html", {'pokemon': pokemon})
    
    return HttpResponse("Nada")
        