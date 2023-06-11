import json

from csv import DictReader

from homework_3.files import USERS_FILE_PATH
from homework_3.files import BOOKS_FILE_PATH
from homework_3.files import RESULT_FILE_PATH


def parse_users() -> list:
    with open(USERS_FILE_PATH, "r") as f:
        reader = json.load(f)
        new_users_list = [
            {
                'name': row['name'],
                'gender': row['gender'],
                'address': row['address'],
                'age': row['age'],
                'books': []
             } for row in reader
        ]
        return new_users_list


def parse_books() -> list:
    with open(BOOKS_FILE_PATH, newline='') as f:
        reader = DictReader(f)
        new_books_list = [
            {
                'title': row['Title'],
                'author': row['Author'],
                'pages': int(row['Pages']),
                'genre': row['Genre']
            } for row in reader
        ]
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
    for book in generate_book:
        if books_count < len(users):
            user = next(generate_user)
            user['books'].append(book)
            result_list.append(user)
            books_count += 1
        else:
            result_list[books_count % len(users)]['books'].append(book)
            books_count += 1
    return result_list


def create_result_file(result_file):
    with open(RESULT_FILE_PATH, "w") as f:
        s = json.dumps(result_file, indent=4)
        f.write(s)


users_list = parse_users()
books_list = parse_books()
result = distribute_books(users_list, books_list)
create_result_file(result)
