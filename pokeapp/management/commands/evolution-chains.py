from django.core.management.base import BaseCommand, CommandError
import requests
from pokeapp.models import Pokemon

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        evolution_chain = requests.get(f'https://pokeapi.co/api/v2/evolution-chain/{options["id"]}/').json()
        
        self.get_evolution_chain(evolution_chain['chain'])
        
        
    def add_arguments(self, parser):
        parser.add_argument(
            'id',
            nargs='?',
            const='1',
            type=str,
            help='id of evolution chain',
        )
    
    def get_pokemon(self, url):
        specie = requests.get(url).json()
        for item in specie['varieties']:
            pokemon = requests.get(item['pokemon']['url']).json()
            print(f' se tranforma en {pokemon["name"]}')
            
            #Pokemon.objects.create()
            
            return pokemon
            break

    def get_evolution_chain(self, chain, pokemon = None):
        print(chain['species']['name'], end='')
        
        if chain['evolves_to']:
            for item in chain['evolves_to']:
                pokemon = self.get_pokemon(item['species']['url'])            
                if item['evolves_to']:
                    self.get_evolution_chain(item, pokemon)