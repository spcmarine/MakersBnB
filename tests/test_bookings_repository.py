from lib.bookings import Bookings
from lib.bookings_repository import BookingsRepository

def test_get_all_booking(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repo = BookingsRepository(db_connection)

    result = repo.all()
    assert result == [
                      Bookings(1, 1, 1, '21-08-2023'),
                      Bookings(2, 2, 2, '22-08-2023'),
                      Bookings(3, 3, 3, '23-08-2023'),
                      Bookings(4, 4, 4, '24-08-2023'),
                      ]
    
def test_create_new_user(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = BookingsRepository(db_connection)

    repository.create(Bookings(None, 5, 5, '24-08-2023'))

    result = repository.all()
    assert result == [
                      Bookings(1, 1, 1, '21-08-2023'),
                      Bookings(2, 2, 2, '22-08-2023'),
                      Bookings(3, 3, 3, '23-08-2023'),
                      Bookings(4, 4, 4, '24-08-2023'),
                      Bookings(5, 5, 5, '24-08-2023')
                      ]
    
def test_delete_record(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = BookingsRepository(db_connection)
    repository.delete(3)

    result = repository.all()
    assert result == [
                      Bookings(1, 1, 1, '21-08-2023'),
                      Bookings(2, 2, 2, '22-08-2023'),
                      Bookings(4, 4, 4, '24-08-2023'),
                      ]