import pytest

from homework_4.src.generated_data import generated_resource


def pytest_addoption(parser):
    parser.addoption(
        '--url',
        default='https://ya.ru',
        help='This is request url'
    )
    parser.addoption(
        '--status_code',
        default=200,
        help='This is expected status code'
    )


@pytest.fixture
def url(request):
    return request.config.getoption('--url')


@pytest.fixture
def status_code(request):
    return request.config.getoption('--status_code')


@pytest.fixture
def get_generated_data():
    return next(generated_resource())
