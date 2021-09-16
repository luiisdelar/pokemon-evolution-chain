from django.core.management.base import BaseCommand, CommandError
import requests
from pokeapp.models import Pokemon, Stats, EvolutionChain

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        evolution_chain = requests.get(f'https://pokeapi.co/api/v2/evolution-chain/{options["id"]}/').json()
        
        self.create_evolution_chain(evolution_chain['chain'])
        
    def add_arguments(self, parser):
        parser.add_argument(
            'id',
            nargs='?',
            const='1',
            type=str,
            help='id of evolution chain',
        )
    
    def create_pokemon(self, url, prev_evolution = None, next_evolution = None):
        specie = requests.get(url).json()
        
        for item in specie['varieties']:
            pokemon = requests.get(item['pokemon']['url']).json()
            print(f' se tranforma en {pokemon["name"]}')

            
            # stats = Stats.objects.create(
            #     hp = pokemon['stats'][0]['base_stat'],
            #     attack = pokemon['stats'][1]['base_stat'],
            #     defense = pokemon['stats'][2]['base_stat'],
            #     special_attack = pokemon['stats'][3]['base_stat'],
            #     special_defense = pokemon['stats'][4]['base_stat'],
            #     speed = pokemon['stats'][5]['base_stat'],
            # )

            # obj_pokemon = Pokemon.objects.create(
            #     iid = pokemon["id"],
            #     name = pokemon["name"],
            #     height = pokemon["height"],
            #     weight = pokemon["weight"],
            #     stats = stats
            # )
            
            evol_chain = EvolutionChain.objects.creaet(
                evols_to = next_evolution,
                prevols_to = prev_evolution
            )

            # return obj_pokemon
            break

    def create_evolution_chain(self, chain, prev_pokemon = None, next_pokemon = None):
        print(chain['species']['name'], end='')
        
        if chain['evolves_to']:
            for item in chain['evolves_to']:
                pokemon = self.create_pokemon(
                    item['species']['url'], 
                    prev_evolution = prev_pokemon, 
                    next_evolution = next_pokemon
                )            
                
                if item['evolves_to']:
                    self.create_evolution_chain(item, pokemon)