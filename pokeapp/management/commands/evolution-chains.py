from django.core.management.base import BaseCommand, CommandError
import requests
from pokeapp.models import EvolsTo, Pokemon, Stats, EvolutionChain

class Command(BaseCommand):
    evol_chain = ''
    cont = True
    
    def handle(self, *args, **options):
        evolution_chain = requests.get(f'https://pokeapi.co/api/v2/evolution-chain/{options["id"]}/').json()

        self.evol_chain = EvolutionChain.objects.create()
        #print(evolution_chain['chain']['species']['url'])
        pokemon, evol_to = self.create_pokemon(url = evolution_chain['chain']['species']['url'])
        self.create_evolution_chain(chain = evolution_chain['chain'], preevolution=pokemon, evol_to=evol_to)
        #self.create_evolution_chain(chain = evolution_chain)
        
    def add_arguments(self, parser):
        parser.add_argument(
            'id',
            nargs='?',
            const='1',
            type=str,
            help='id of evolution chain',
        )
    
    def create_pokemon(self, url, preevolution = None, evol_to = None):
        specie = requests.get(url).json()

        for item in specie['varieties']:
            pokemon = requests.get(item['pokemon']['url']).json()
            #print(f' se tranforma en {pokemon["name"]}')
            
            stats = Stats.objects.create(
                hp = pokemon['stats'][0]['base_stat'],
                attack = pokemon['stats'][1]['base_stat'],
                defense = pokemon['stats'][2]['base_stat'],
                special_attack = pokemon['stats'][3]['base_stat'],
                special_defense = pokemon['stats'][4]['base_stat'],
                speed = pokemon['stats'][5]['base_stat'],
            )

            obj_pokemon = Pokemon.objects.create(
                iid = pokemon["id"],
                name = pokemon["name"],
                height = pokemon["height"],
                weight = pokemon["weight"],
                stats = stats,
                evolution_chain = self.evol_chain
            )
            
            if evol_to:
                evol_to.pokemon = preevolution
                new_evol = EvolsTo.objects.create(pokemon = obj_pokemon)
                evol_to.evols_to = new_evol
                evol_to.save()
                evol_to = new_evol

            if preevolution == None and evol_to == None:
                evol_to = EvolsTo.objects.create(pokemon = obj_pokemon)
                self.evol_chain.evolutions = evol_to
                self.evol_chain.save()
    
            print(f'Save data of: {obj_pokemon.name}')
            return obj_pokemon, evol_to
            
    def create_evolution_chain(self, chain, preevolution = None, evol_to = None):
        #print(chain['species']['name'], end='')
        
         
        if chain['evolves_to']:
            for item in chain['evolves_to']:
                pokemon, evol_to = self.create_pokemon(
                    item['species']['url'],
                    preevolution = preevolution,
                    evol_to = evol_to 
                )
                          
                if item['evolves_to']:
                    # evol_pokemon add evol_to pokemon
                    self.create_evolution_chain(chain = item, preevolution = pokemon, evol_to = evol_to)