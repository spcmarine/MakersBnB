from lib.bookings import Bookings

class BookingsRepository:
    def __init__(self, connection):
        self.connection = connection
    def all(self):
        booking = self.connection.execute("SELECT * FROM bookings")
        bookings_list = [Bookings(i['id'], i['spacesid'], i['usersid'], i['dates_of_booking']) for i in booking]
        return bookings_list

    def create(self, booking):
        self.connection.execute('INSERT INTO bookings (spacesID, usersID, dates_of_booking) VALUES (%s, %s, %s)', [booking.spacesID, booking.usersID, booking.dates_of_booking])

    def delete(self, id):
        self.connection.execute('DELETE FROM bookings WHERE id = %s', [id])
        