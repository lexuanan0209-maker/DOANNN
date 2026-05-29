import tkinter as tk
from tkinter import messagebox


class RoomStatusWindow:

    def __init__(
        self,
        room,
        room_service,
        refresh_callback
    ):

        self.room = room

        self.room_service = room_service

        self.refresh_callback = refresh_callback

        self.window = tk.Toplevel()

        self.window.title("Quản lý trạng thái phòng")

        self.window.geometry("350x300")

        self.window.configure(bg="#181A1F")

        tk.Label(
            self.window,
            text=f"PHÒNG {room.room_id}",
            font=("Arial", 18, "bold"),
            bg="#181A1F",
            fg="white"
        ).pack(pady=20)

        tk.Label(
            self.window,
            text=f"Trạng thái hiện tại: {room.status}",
            font=("Arial", 12),
            bg="#181A1F",
            fg="white"
        ).pack(pady=10)

        btn_clean = tk.Button(
            self.window,
            text="🧹 Đang dọn",
            bg="#F59E0B",
            fg="white",
            font=("Arial", 11, "bold"),
            width=20,
            height=2,
            command=lambda: self.update_status(
                "Đang dọn"
            )
        )

        btn_clean.pack(pady=10)

        btn_maintain = tk.Button(
            self.window,
            text="🛠 Bảo trì",
            bg="gray",
            fg="white",
            font=("Arial", 11, "bold"),
            width=20,
            height=2,
            command=lambda: self.update_status(
                "Bảo trì"
            )
        )

        btn_maintain.pack(pady=10)

        btn_available = tk.Button(
            self.window,
            text="✅ Trống",
            bg="green",
            fg="white",
            font=("Arial", 11, "bold"),
            width=20,
            height=2,
            command=lambda: self.update_status(
                "Trống"
            )
        )

        btn_available.pack(pady=10)

    def update_status(self, status):

        self.room_service.update_room_status(
            self.room,
            status
        )

        messagebox.showinfo(
            "Thông báo",
            "Cập nhật trạng thái thành công"
        )

        self.refresh_callback()

        self.window.destroy()