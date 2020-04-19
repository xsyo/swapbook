from collections import namedtuple

BookTuple = namedtuple('BookTuple', ['book_object', 'city_user'])


def get_users_in_my_city(user, book):
    city = user.city
    users = book.holders.filter(city=city)
    return users

