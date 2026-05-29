from models.booking import Booking
from models.customer import Customer

from utils.file_handler import (
    load_json,
    save_json
)

from utils.validator import validate_date

from exceptions.custom_exceptions import (
    RoomNotAvailableError
)

BOOKING_FILE = 'data/bookings.json'


class BookingService:

    def __init__(self, room_service):

        self.room_service = room_service

        data = load_json(BOOKING_FILE)

        self.bookings = data if data else []

    def checkin(
        self,
        room,
        name,
        cccd,
        phone,
        checkin,
        checkout
    ):

        if room.status != 'Trống':

            raise RoomNotAvailableError(
                'Phòng không khả dụng'
            )

        validate_date(
            checkin,
            checkout
        )

        customer = Customer(
            name,
            cccd,
            phone
        )

        booking = Booking(
            customer,
            room,
            checkin,
            checkout
        )

        self.bookings.append(
            booking.to_dict()
        )

        room.status = 'Đang ở'

        self.room_service.save_rooms()

        self.save_bookings()

    def checkout(self, room):

        for booking in self.bookings:

            if (
                booking["room_id"]
                ==
                room.room_id
            ):

                if booking.get("status") != "Đã thanh toán":

                    days = 1

                    total_price = (
                        room.base_price * days
                    )

                    booking["total_price"] = total_price

                    booking["status"] = "Đã thanh toán"

        room.status = 'Trống'

        self.room_service.save_rooms()

        self.save_bookings()

    def save_bookings(self):

        save_json(
            BOOKING_FILE,
            self.bookings
        )