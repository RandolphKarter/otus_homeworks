import json

from csv import DictReader

from homework_3.files import USERS_FILE_PATH
from homework_3.files import BOOKS_FILE_PATH
from homework_3.files import RESULT_FILE_PATH


def parse_users() -> list:
    with open(USERS_FILE_PATH, "r") as f:
        reader = json.load(f)
        new_users_list = []
        for row in reader:
            user = {'name': row['name'], 'gender': row['gender'], 'address': row['address'], 'age': row['age'],
                    'books': []}
            new_users_list.append(user)
        return new_users_list


def parse_books() -> list:
    with open(BOOKS_FILE_PATH, newline='') as f:
        reader = DictReader(f)
        new_books_list = []
        for row in reader:
            book = {'title': row['Title'], 'author': row['Author'], 'pages': int(row['Pages']), 'genre': row['Genre']}
            new_books_list.append(book)
        return new_books_list


def generator(some_list: list):
    for i in range(len(some_list)):
        item = some_list[i]
        yield item


def distribute_books(users: list, books: list):
    result_list = []
    generate_user = generator(users)
    generate_book = generator(books)
    books_count = 0
    while books_count < len(books):
        if books_count < len(users):
            user = next(generate_user)
            book = next(generate_book)
            user['books'].append(book)
            result_list.append(user)
            books_count += 1
        elif books_count >= len(users):
            for user in result_list:
                if books_count < len(books):
                    book = next(generate_book)
                    user['books'].append(book)
                    books_count += 1

    with open(RESULT_FILE_PATH, "w") as f:
        s = json.dumps(result_list, indent=4)
        f.write(s)


users_list = parse_users()
books_list = parse_books()
distribute_books(users_list, books_list)
