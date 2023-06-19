import pytest
import requests


@pytest.mark.parametrize('repeat', range(5))
def test_get_resource_by_id(get_generated_data, repeat):
    r = requests.get(f'https://jsonplaceholder.typicode.com/posts/{get_generated_data["id"]}')
    assert r.status_code == 200, f'Expected status code 200, return {r.status_code}'
    assert get_generated_data['id'] == r.json()['id'], 'Expected id not found in response'


@pytest.mark.parametrize('repeat', range(5))
def test_creating_resource(get_generated_data, repeat):
    r = requests.post('https://jsonplaceholder.typicode.com/posts', json={"title": get_generated_data["title"],
                                                                          "body": get_generated_data["body"],
                                                                          "userId": get_generated_data["userId"]})
    assert r.status_code == 201, f'Expected status code 201, return {r.status_code}'
    assert get_generated_data["title"] == r.json()["title"], 'Expected title not found in response'
    assert get_generated_data["body"] == r.json()["body"], 'Expected body not found in response'
    assert get_generated_data["userId"] == r.json()["userId"], 'Expected userId not found in response'


@pytest.mark.parametrize('repeat', range(5))
def test_updating_resource(get_generated_data, repeat):
    r = requests.put(f'https://jsonplaceholder.typicode.com/posts/{get_generated_data["id"]}', json=get_generated_data)
    assert r.status_code == 200, f'Expected status code 200, return {r.status_code}'
    assert get_generated_data["title"] == r.json()["title"], 'Expected title not found in response'
    assert get_generated_data["body"] == r.json()["body"], 'Expected body not found in response'
    assert get_generated_data["userId"] == r.json()["userId"], 'Expected userId not found in response'


@pytest.mark.parametrize('repeat', range(5))
def test_patching_resource(get_generated_data, repeat):
    r = requests.patch(f'https://jsonplaceholder.typicode.com/posts/{get_generated_data["id"]}',
                       json={"title": get_generated_data["title"]})
    assert r.status_code == 200, f'Expected status code 200, return {r.status_code}'
    assert get_generated_data["title"] == r.json()["title"], 'Expected title not found in response'
    assert get_generated_data["id"] == r.json()["id"], 'Expected id not found in response'


@pytest.mark.parametrize('repeat', range(5))
def test_delete_resource(get_generated_data, repeat):
    r = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{get_generated_data["id"]}')
    assert r.status_code == 200, f'Expected status code 200, return {r.status_code}'
    assert r.json() == {}, f'Expected empty response, got {r.json()}'
