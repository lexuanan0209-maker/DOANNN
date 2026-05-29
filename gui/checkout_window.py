import tkinter as tk
from tkinter import messagebox


class CheckoutWindow:

    def __init__(
        self,
        room,
        booking_service,
        refresh_callback
    ):

        self.room = room

        self.booking_service = booking_service

        self.refresh_callback = refresh_callback

        self.window = tk.Toplevel()

        self.window.title("Check Out")

        self.window.geometry("350x250")

        tk.Label(
            self.window,
            text=f"CHECK OUT PHÒNG {room.room_id}",
            font=("Arial", 16, "bold")
        ).pack(pady=20)

        tk.Label(
            self.window,
            text=f"Loại phòng: {room.room_type}"
        ).pack(pady=5)

        tk.Label(
            self.window,
            text=f"Giá niêm yết: {room.base_price:,} VNĐ"
        ).pack(pady=5)

        tk.Button(
            self.window,
            text="XÁC NHẬN CHECK OUT",
            bg="red",
            fg="white",
            width=25,
            height=2,
            command=self.checkout
        ).pack(pady=25)

    def checkout(self):

        self.booking_service.checkout(
            self.room
        )

        messagebox.showinfo(
            "Thành công",
            "Check out thành công"
        )

        self.refresh_callback()

        self.window.destroy()