from unittest.mock import Mock
from tests.conftest import *
from lib.database_connection import * 
from lib.spaces_repository import *
from lib.spaces import *

def test_return_spaces(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = Spacerepository(db_connection)
    actual_spaces = repository.all()
    expected_spaces = [
        Spaces(1, 'danHouse', 'Located on the Beach', 20, 1),
        Spaces(2, 'khalifaHouse', 'Central Location', 15, 2),
        Spaces(3, 'tomHouse', 'toursity location', 80, 3),
        Spaces(4, 'lilyHouse', 'located in a lovely touristy village', 90, 4)
    ]
    assert actual_spaces == expected_spaces

    
def test_price_less_than(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = Spacerepository(db_connection)
    actual_spaces = repository.price_sort_less_than(20)
    expected_spaces = [
        Spaces(1, 'danHouse', 'Located on the Beach', 20, 1),
        Spaces(2, 'khalifaHouse', 'Central Location', 15, 2)
    ]
    assert actual_spaces == expected_spaces

def test_return_all_added(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = Spacerepository(db_connection)
    space = Spaces(None, 'leoHouse', 'country side', 110, 1)
    repository.add(space)
    actual_spaces = repository.all()
    expected_spaces = [
        Spaces(1, 'danHouse', 'Located on the Beach', 20, 1),
        Spaces(2, 'khalifaHouse', 'Central Location', 15, 2),
        Spaces(3, 'tomHouse', 'toursity location', 80, 3),
        Spaces(4, 'lilyHouse', 'located in a lovely touristy village', 90, 4),
        Spaces(5, 'leoHouse', 'country side', 110, 1)
    ]
    assert actual_spaces == expected_spaces

def test_remove_function(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = Spacerepository(db_connection)
    space = 4
    repository.remove(space)
    actual_spaces = repository.all()
    expected_spaces = [
        Spaces(1, 'danHouse', 'Located on the Beach', 20, 1),
        Spaces(2, 'khalifaHouse', 'Central Location', 15, 2),
        Spaces(3, 'tomHouse', 'toursity location', 80, 3)
    ]
    assert actual_spaces == expected_spaces


#21-08-2023
def test_search_date(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = Spacerepository(db_connection)
    actual_spaces = repository.search_date('21-08-2023')
    expected_spaces = [
        Spaces(2, 'khalifaHouse', 'Central Location', 15, 2),
        Spaces(3, 'tomHouse', 'toursity location', 80, 3),
        Spaces(4, 'lilyHouse', 'located in a lovely touristy village', 90, 4)
    ]
    assert actual_spaces == expected_spaces