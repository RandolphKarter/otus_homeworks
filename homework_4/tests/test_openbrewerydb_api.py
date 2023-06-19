import random
import pytest
import requests


@pytest.mark.parametrize('brewery_id, brewery_name',
                         [
                            ('5128df48-79fc-4f0f-8b52-d06be54d0cec', '(405) Brewing Co'),
                            ('6d14b220-8926-4521-8d19-b98a2d6ec3db', '10 Barrel Brewing Co'),
                            ('1ecc330f-6275-42a5-b14e-00adbed62752', '10 Torr Distilling and Brewing'),
                            ('5ae467af-66dc-4d7f-8839-44228f89b596', '101 North Brewing Company'),
                            ('e5f3e72a-fee2-4813-82cf-f2e53b439ae6', '12 Acres Brewing Company')
                         ])
def test_get_single_brewery(brewery_id, brewery_name):
    r = requests.get(f'https://api.openbrewerydb.org/v1/breweries/{brewery_id}')
    assert r.status_code == 200, f'Expected status code 200, return {r.status_code}'
    assert brewery_id == r.json()['id'], 'Expected id not found in response'
    assert brewery_name == r.json()['name'], 'Expected name not found in response'


@pytest.mark.parametrize('repeat', range(5))
def test_get_brewery_list(repeat):
    random_amount = random.randint(1, 20)
    r = requests.get(f'https://api.openbrewerydb.org/v1/breweries?per_page={random_amount}')
    assert r.status_code == 200, f'Expected status code 200, return {r.status_code}'
    assert random_amount == len(r.json()), 'Expected amount of breweries dont equal sent value'


@pytest.mark.parametrize('brewery_city, amount',
                         [
                             ('Portland', random.randint(1, 20)),
                             ('Denver', random.randint(1, 20)),
                             ('Knoxville', random.randint(1, 20)),
                             ('Bend', random.randint(1, 20)),
                             ('Tucson', random.randint(1, 19)),
                         ])
def test_get_brewery_by_city_and_random_amount(brewery_city, amount):
    r = requests.get(f'https://api.openbrewerydb.org/v1/breweries?by_city={brewery_city}&per_page={amount}')
    assert r.status_code == 200, f'Expected status code 200, return {r.status_code}'
    for item in r.json():
        assert brewery_city in item['city'], 'Expected city not found in response'
    assert int(amount) == len(r.json()), 'Expected amount of breweries dont equal sent value'


@pytest.mark.parametrize('type, amount',
                         [
                             ('micro', random.randint(1, 20)),
                             ('regional', random.randint(1, 20)),
                             ('planning', random.randint(1, 20)),
                             ('bar', random.randint(1, 4)),
                             ('closed', random.randint(1, 20))
                         ])
def test_get_brewery_by_type(type, amount):
    r = requests.get(f'https://api.openbrewerydb.org/v1/breweries?by_type={type}&per_page={amount}')
    assert r.status_code == 200, f'Expected status code 200, return {r.status_code}'
    for item in r.json():
        assert type in item['brewery_type'], 'Expected brewery type not found in response'
    assert int(amount) == len(r.json()), 'Expected amount of breweries dont equal sent value'


@pytest.mark.parametrize('state, amount',
                         [
                             ('new_york', random.randint(1, 20)),
                             ('texas', random.randint(1, 20)),
                             ('massachusetts', random.randint(1, 20)),
                             ('colorado', random.randint(1, 20)),
                             ('california', random.randint(1, 20))
                         ])
def test_get_brewery_by_state(state, amount):
    r = requests.get(f'https://api.openbrewerydb.org/v1/breweries?by_state={state}&per_page={amount}')
    assert r.status_code == 200, f'Expected status code 200, return {r.status_code}'
    for item in r.json():
        assert state.replace('_', ' ') in item['state'].lower(), 'Expected state not found in response'
    assert int(amount) == len(r.json()), 'Expected amount of breweries dont equal sent value'
