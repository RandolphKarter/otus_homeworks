from dataclasses import dataclass
from faker import Faker
import random


@dataclass
class Resource:
    id: int = None
    title: str = None
    body: str = None
    userId: int = None


def generated_resource():
    faker_ru = Faker('ru_RU')
    Faker.seed()
    yield vars(Resource(
        id=random.randint(1, 100),
        title=faker_ru.text(max_nb_chars=20),
        body=faker_ru.text(max_nb_chars=50),
        userId=random.randint(1, 1000),
    ))
