from lib.bookings import Bookings


def test_booking_construct():
    user = Bookings(1, '1', '1', '21-08-2023')
    assert user.id == 1
    assert user.spacesID == '1'
    assert user.usersID == '1'
    assert user.dates_of_booking == '21-08-2023'

def test_booking_are_equal():
    user1 = Bookings(1, '1', '1', '21-08-2023')
    user2 = Bookings(1, '1', '1', '21-08-2023')
    assert user1 == user2

def test_booking_format_nicely():
    user = Bookings(1, '1', '1', '21-08-2023')
    assert str(user) == "Bookings(1, 1, 1, 21-08-2023)"