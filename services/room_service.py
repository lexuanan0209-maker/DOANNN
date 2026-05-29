from models.room import StandardRoom, VIPRoom, SuiteRoom
from utils.file_handler import load_json, save_json

ROOM_FILE = 'data/rooms.json'


class RoomService:

    def __init__(self):

        self.rooms = []

        self.load_rooms()

    # =========================
    # LOAD ROOMS
    # =========================

    def load_rooms(self):

        data = load_json(ROOM_FILE)

        if not data:

            self.create_default_rooms()

            return

        for r in data:

            room = self.create_room_object(r)

            self.rooms.append(room)

    # =========================
    # CREATE DEFAULT ROOMS
    # =========================

    def create_default_rooms(self):

        for i in range(1, 6):

            self.rooms.append(
                StandardRoom(
                    f"1{i}",
                    "Standard",
                    "Trống",
                    500000,
                    1
                )
            )

        for i in range(1, 6):

            self.rooms.append(
                VIPRoom(
                    f"2{i}",
                    "VIP",
                    "Trống",
                    1000000,
                    2
                )
            )

        for i in range(1, 4):

            self.rooms.append(
                SuiteRoom(
                    f"3{i}",
                    "Suite",
                    "Trống",
                    2000000,
                    3
                )
            )

        self.save_rooms()

    # =========================
    # CREATE ROOM OBJECT
    # =========================

    def create_room_object(self, r):

        if r['room_type'] == 'Standard':

            return StandardRoom(**r)

        if r['room_type'] == 'VIP':

            return VIPRoom(**r)

        return SuiteRoom(**r)

    # =========================
    # SAVE ROOMS
    # =========================

    def save_rooms(self):

        save_json(
            ROOM_FILE,
            [room.to_dict() for room in self.rooms]
        )

    # =========================
    # FIND EMPTY ROOMS
    # =========================

    def find_empty_rooms(
        self,
        room_type=None
    ):

        result = []

        for room in self.rooms:

            if room.status == 'Trống':

                if (
                    room_type is None
                    or
                    room.room_type == room_type
                ):

                    result.append(room)

        return result

    # =========================
    # UPDATE ROOM STATUS
    # =========================

    def update_room_status(
        self,
        room,
        status
    ):

        room.status = status

        self.save_rooms()