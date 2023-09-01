from lib.users import User


def test_users_construct():
    user = User(1, 'khalifa13231', 'khalifa fadel', '12344312')
    assert user.id == 1
    assert user.username == 'khalifa13231'
    assert user.fullname == 'khalifa fadel'
    assert user.password == '12344312'

def test_users_are_equal():
    user1 = User(1, 'khalifa13231', 'khalifa fadel', '12344312')
    user2 = User(1, 'khalifa13231', 'khalifa fadel', '12344312')
    assert user1 == user2

def test_user_format_nicely():
    user = User(1, 'khalifa13231', 'khalifa fadel', '12344312')
    assert str(user) == "User(1, khalifa13231, khalifa fadel, 12344312)"