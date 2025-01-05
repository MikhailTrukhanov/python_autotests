import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3a552557762934c87f14049f728f36c3'
HEADER = {'Content-type' : 'Application/json' , 'trainer_token' : TOKEN}

body_create = {
    "name": "generate",
    "photo_id": -1
}

body_change_name = {
    "pokemon_id": "152056",
    "name": "Grisha"
}

body_add = {
    "pokemon_id": "152056"
}

'''response_create = requests.post(url = f'{URL}/pokemons' , headers = HEADER , json = body_create)
print(response_create.text)'''

'''response_change = requests.patch(url = f'{URL}/pokemons' , headers = HEADER , json = body_change_name)
print(response_change.text)'''

response_add = requests.post(url = f'{URL}/trainers/add_pokeball' ,  headers = HEADER , json = body_add )
print(response_add.text)