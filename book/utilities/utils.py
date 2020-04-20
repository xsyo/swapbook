from collections import namedtuple

BookTuple = namedtuple('BookTuple', ['book_object', 'city_user'])


def get_users_in_my_city(user, book):
    if user.is_authenticated:
        city = user.city
        users = book.holders.filter(city=city)
        return users
    else:
        return book.holders.all()

