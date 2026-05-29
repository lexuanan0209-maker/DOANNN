
from collections import defaultdict
from datetime import datetime

from utils.file_handler import load_json


BOOKING_FILE = "data/bookings.json"


class RevenueService:

    def __init__(self):

        self.bookings = load_json(
            BOOKING_FILE
        )

    def revenue_by_day(self):

        revenue = defaultdict(int)

        for booking in self.bookings:

            checkout = booking["checkout"]

            total = booking.get(
                "total_price",
                0
            )

            revenue[checkout] += total

        return revenue

    def revenue_by_month(self):

        revenue = defaultdict(int)

        for booking in self.bookings:

            checkout = booking["checkout"]

            total = booking.get(
                "total_price",
                0
            )

            month = datetime.strptime(
                checkout,
                "%Y-%m-%d"
            ).strftime("%Y-%m")

            revenue[month] += total

        return revenue

    def revenue_by_year(self):

        revenue = defaultdict(int)

        for booking in self.bookings:

            checkout = booking["checkout"]

            total = booking.get(
                "total_price",
                0
            )

            year = datetime.strptime(
                checkout,
                "%Y-%m-%d"
            ).strftime("%Y")

            revenue[year] += total

        return revenue