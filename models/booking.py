
class Booking:

    def __init__(
        self,
        customer,
        room,
        checkin,
        checkout
    ):

        self.customer = customer
        self.room = room

        self.checkin = checkin
        self.checkout = checkout

    def to_dict(self):

        return {

            "customer": self.customer.to_dict(),

            "room_id": self.room.room_id,

            "checkin": self.checkin,

            "checkout": self.checkout
        }

