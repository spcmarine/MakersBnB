from lib.database_connection import *
from lib.spaces import *
from lib.bookings import *

class Spacerepository():
    def __init__(self, connection):
        self._connection = connection

    #returns all spaces
    def all(self):
        rows = self._connection.execute('SELECT * from spaces')
        spaces = []
        for row in rows:
            item = Spaces(row["id"], row["spacename"], row["description"], row["price"], row["usersid"])
            spaces.append(item)
        return spaces
    
    #returns avalibilty of given date
    def search_date(self, date):
        rows = self._connection.execute(f"SELECT * FROM spaces RIGHT JOIN bookings ON spaces.id = bookings.spacesid WHERE bookings.dates_of_booking <> '{date}'")
        spaces = []
        for row in rows:
            item = Spaces(row["id"], row["spacename"], row["description"], row["price"], row["usersid"])
            spaces.append(item)
        return spaces

    #returns price less than or equal to
    def price_sort_less_than(self, price):
        rows = self._connection.execute(f'SELECT * from spaces WHERE price <= {price}')
        spaces = []
        for row in rows:
            item = Spaces(row["id"], row["spacename"], row["description"], row["price"], row["usersid"])
            spaces.append(item)
        return spaces

    #more than option?

    #add function - adds space to database to be rented out
    def add(self, space):
        self._connection.execute("INSERT INTO spaces (spacename, description, price, usersid) VALUES (%s, %s, %s, %s)",
        [space.space_name, space.description, space.price, space.userID])
        return None

    #remove function - removes specific location at request of user
    def remove(self, spaceID):
        self._connection.execute(
            'DELETE FROM spaces WHERE id = %s', [spaceID])
        return None

    #Edit entry?