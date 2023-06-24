import random
import pytest
import requests


@pytest.mark.parametrize('repeat', range(5))
def test_single_random_image(repeat):
    r = requests.get('https://dog.ceo/api/breeds/image/random')
    assert r.status_code == 200, f'Expected status code 200, return {r.status_code}'
    assert 'images.dog.ceo' in r.json()['message'], 'Expected domain images.dog.ceo in response text'
    assert 'jpg' in r.json()['message'], 'Expected file format jpg in response text'


@pytest.mark.parametrize('repeat', range(5))
def test_multiple_random_images(repeat):
    random_amount = random.randint(1, 50)
    r = requests.get(f'https://dog.ceo/api/breeds/image/random/{random_amount}')
    assert r.status_code == 200, f'Expected status code 200, return {r.status_code}'
    assert random_amount == len(r.json()['message']), 'Expected amount of images dont equal sent value'


@pytest.mark.parametrize('breed', ['akita', 'bulldog', 'ovcharka', 'spaniel', 'dingo'])
def test_single_image_from_breed_collection(breed):
    r = requests.get(f'https://dog.ceo/api/breed/{breed}/images/random')
    assert r.status_code == 200, f'Expected status code 200, return {r.status_code}'
    assert breed in r.json()['message'], 'Expected breed in response url not found'


@pytest.mark.parametrize('breed, sub_breed',
                         [
                             ('bulldog', 'boston'),
                             ('spaniel', 'sussex'),
                             ('hound', 'blood'),
                             ('bulldog', 'french'),
                             ('terrier', 'fox')
                         ])
def test_single_image_from_sub_breed_collection(breed, sub_breed):
    r = requests.get(f'https://dog.ceo/api/breed/{breed}/{sub_breed}/images/random')
    assert r.status_code == 200, f'Expected status code 200, return {r.status_code}'
    assert f'{breed}-{sub_breed}' in r.json()['message'], 'Expected sub breed in response url not found'


@pytest.mark.parametrize('breed, sub_breed, amount',
                         [
                             ('bulldog', 'french', random.randint(1, 20)),
                             ('spaniel', 'cocker', random.randint(1, 20)),
                             ('hound', 'ibizan', random.randint(1, 20)),
                             ('setter', 'gordon', random.randint(1, 20)),
                             ('terrier', 'irish', random.randint(1, 20)),
                         ])
def test_multiple_image_from_sub_breed_collection(breed, sub_breed, amount):
    r = requests.get(f'https://dog.ceo/api/breed/{breed}/{sub_breed}/images/random/{amount}')
    assert r.status_code == 200, f'Expected status code 200, return {r.status_code}'
    for item in r.json()['message']:
        assert f'{breed}-{sub_breed}' in item, 'Expected sub breed in response url not found'
    assert amount == len(r.json()["message"]), 'Expected amount of images dont equal sent value'

