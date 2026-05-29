
import tkinter as tk

from gui.room_status_window import RoomStatusWindow


class RoomGrid:

    def __init__(

        self,

        root,

        rooms,

        on_click,

        room_service,

        refresh_callback,

        current_user
    ):

        self.root = root

        self.rooms = rooms

        self.on_click = on_click

        self.room_service = room_service

        self.refresh_callback = refresh_callback

        self.current_user = current_user

    # =========================
    # DRAW GRID
    # =========================

    def draw(self):

        for widget in self.root.winfo_children():

            widget.destroy()

        row = 0

        col = 0

        for room in self.rooms:

            color = "green"

            if room.status == "Đang ở":

                color = "red"

            elif room.status == "Đang dọn":

                color = "yellow"

            elif room.status == "Bảo trì":

                color = "gray"

            button = tk.Button(

                self.root,

                text=(
                    f"Phòng: {room.room_id}\n"
                    f"{room.room_type}\n"
                    f"{room.status}"
                ),

                width=18,

                height=6,

                bg=color,

                fg="white",

                font=("Arial", 10, "bold"),

                relief="flat",

                cursor="hand2",

                command=lambda r=room:
                self.on_click(r)
            )

            button.grid(

                row=row,

                column=col,

                padx=15,

                pady=15
            )

            # CLICK PHẢI -> ĐỔI TRẠNG THÁI

            button.bind(

                "<Button-3>",

                lambda e, r=room:
                self.open_status_window(r)
            )

            col += 1

            if col == 4:

                col = 0

                row += 1

    # =========================
    # OPEN STATUS WINDOW
    # =========================

    def open_status_window(self, room):

        if (
            self.current_user
            and
            self.current_user["role"] in [
                "admin",
                "staff"
            ]
        ):

            RoomStatusWindow(

                room,

                self.room_service,

                self.refresh_callback
            )

