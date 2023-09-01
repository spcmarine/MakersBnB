from lib.users import User
from lib.users_repository import UserRepository


def test_get_all_users(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repo = UserRepository(db_connection)

    result = repo.all()

    assert result == [User(1, 'dan123', 'Dan Gibson', '123321'),
                      User(2, 'khalifa123', 'Khalifa Fadel', '123321'),
                      User(3, 'tom123', 'Tom Whelan', '123321'),
                      User(4, 'lily123', 'Lily Barton', '123321')]


def test_create_new_user(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = UserRepository(db_connection)

    repository.create(User(None, 'John123', 'John Bar', '123321'))

    result = repository.all()
    assert result == [
        User(1, 'dan123', 'Dan Gibson', '123321'),
        User(2, 'khalifa123', 'Khalifa Fadel', '123321'),
        User(3, 'tom123', 'Tom Whelan', '123321'),
        User(4, 'lily123', 'Lily Barton', '123321'),
        User(5, 'John123', 'John Bar', '123321')
    ]

def test_delete_record(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = UserRepository(db_connection)
    repository.delete(3)

    result = repository.all()
    assert result == [
        User(1, 'dan123', 'Dan Gibson', '123321'),
        User(2, 'khalifa123', 'Khalifa Fadel', '123321'),
        User(4, 'lily123', 'Lily Barton', '123321')
    ]