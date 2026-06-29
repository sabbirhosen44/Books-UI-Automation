import random


def get_random_books(
        books,
        count=5
):

    return random.sample(
        books,
        count
    )