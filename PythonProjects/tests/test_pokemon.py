import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3a552557762934c87f14049f728f36c3'
HEADER = {'Content-type' : 'Application/json' , 'trainer_token' : TOKEN}
TRAINER_ID = '14973'

def test_ststus_code():
    response = requests.get(url = f'{URL}/trainers' , headers = HEADER)
    assert response.status_code == 200

def test_trainer_name():
    response_name = requests.get(url = f'{URL}/trainers' , headers = HEADER , params = {'trainer_id' : TRAINER_ID})
    assert response_name.json()["data"][0]["trainer_name"] == 'Михаил'
