class Bookings:
    def __init__(self, id, spacesID, usersID, dates_of_booking):
        self.id = id
        self.spacesID = spacesID
        self.usersID = usersID
        self.dates_of_booking = dates_of_booking
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Bookings({self.id}, {self.spacesID}, {self.usersID}, {self.dates_of_booking})"