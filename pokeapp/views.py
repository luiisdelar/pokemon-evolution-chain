from django.http.response import JsonResponse
from django.shortcuts import render
from pokeapp.models import Pokemon
from django.http import JsonResponse

# Create your views here.

def search(request, to_search):
    """ search for pokemons matching keyword to_search

    Args:
        request (Request): request 
        to_search (str): parameter to search received by url

    Returns:
        JsonResponse: object of type json with pokemons matches
    """
    json = {}
    cont = 0
    pokemons = Pokemon.objects.filter(name__icontains=to_search)
    
    for pokemon in pokemons:
        index = f'pokemon-{pokemon.iid}'
       
        json[cont] = ({ 
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
        
        evolution_sub_json = { 
            "pokemon": evolution2.pokemon.name, 
            "evols_to": None 
        }        
        
        evolution_json = {
            "pokemon": evolution1.pokemon.name,
            "evols_to": evolution_sub_json
        }
        
        json[cont]["evolution_chain"] = evolution_json
        
        if evolution2.evols_to:
            evolution_sub_json["evols_to"] = {
                "pokemon":evolution2.evols_to.pokemon.name,
                "evols_to": None
            }
        cont += 1
        
    if json == {}:
        return JsonResponse({"message":"Pokemons not found"})
    
    return JsonResponse(json)
        