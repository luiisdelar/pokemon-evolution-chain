# Pokemon Evolution Chain

_Backend test_


### Clone repository 

```
$ git clone https://github.com/luiisdelar/pokemon-evolution-chain.git
```


### Create / Activate development environment (Windows)

```
$ virtualenv env
```

_Then you must activate the development environment_

```
$ source env/Scripts/activate
```

_Finally we are located inside the project folder_

```
$ cd pokemon-evolution-chain/
```


### Instalations  

_Now we must install the project requirements_

```
$ pip install -r requirements.txt
```

### Database Postgres

_Create database in postgres that has as name_

```
db_pokemon
```

### Migrations

_Now the tables are created in the database with the migration_

```
$ python manage.py migrate
```

# Command "evolution-chains"

_To execute the command that saves the data of the evolution chain we use the following command that receives an id as an argument, in example 1_

```
$ python manage.py evolution-chains 1
```

_For more info about command type_

```
$ python manage.py evolution-chains --help
```

_After this you would have the info of the pokemons of the evolution chain stored in the database_

## Get Pokemons 

_At this point we must turn on the server to have the service active_

```
$ python manage.py runserver
```

_to search for pokemons we must use the following route which receives the name of a pokemon by parameter, it returns the possible matches in JSON format_

```
http://localhost:8000/pokemon/{pokemon_name}
```

---
⌨️ con ❤️ por [Luis Ortega](https://github.com/luiisdelar) 😊
