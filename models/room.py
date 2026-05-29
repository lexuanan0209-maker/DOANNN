class Room:
    def __init__(self, room_id, room_type, status, base_price, floor):
        self.room_id = room_id
        self.room_type = room_type
        self.status = status
        self.base_price = base_price
        self.floor = floor

    def calculate_price(self, days):
        return self.base_price * days

    def to_dict(self):
        return {
            "room_id": self.room_id,
            "room_type": self.room_type,
            "status": self.status,
            "base_price": self.base_price,
            "floor": self.floor
        }


class StandardRoom(Room):
    def calculate_price(self, days):
        return self.base_price * days


class VIPRoom(Room):
    def calculate_price(self, days):
        return self.base_price * 1.5 * days


class SuiteRoom(Room):
    def calculate_price(self, days):
        return (self.base_price * 2 * days) + 500000