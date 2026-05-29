import tkinter as tk
from tkinter import messagebox

# =========================
# COLORS
# =========================

BG_COLOR = "#181A1F"
CARD_COLOR = "#1F2937"
PRIMARY = "#2563EB"

TEXT_WHITE = "white"
TEXT_GRAY = "#D1D5DB"

INPUT_BG = "#374151"

SUCCESS = "#10B981"
DANGER = "#DC2626"


class CheckinWindow:

    def __init__(
        self,
        room,
        booking_service,
        refresh_callback
    ):

        self.room = room

        self.booking_service = booking_service

        self.refresh_callback = refresh_callback

        # =========================
        # WINDOW
        # =========================

        self.window = tk.Toplevel()

        self.window.title("Check In")

        self.window.configure(bg=BG_COLOR)

        self.window.resizable(False, False)

        # =========================
        # RESPONSIVE
        # =========================

        screen_width = self.window.winfo_screenwidth()

        screen_height = self.window.winfo_screenheight()

        # MOBILE / TABLET

        if screen_width <= 768:

            window_width = int(screen_width * 0.95)

            window_height = int(screen_height * 0.90)

            title_font = ("Arial", 18, "bold")

            input_font = ("Arial", 11)

            button_font = ("Arial", 11, "bold")

            header_height = 80

        # PC / LAPTOP

        else:

            window_width = 600

            window_height = 650

            title_font = ("Arial", 22, "bold")

            input_font = ("Arial", 12)

            button_font = ("Arial", 12, "bold")

            header_height = 100

        # CENTER WINDOW

        x = (screen_width // 2) - (window_width // 2)

        y = (screen_height // 2) - (window_height // 2)

        self.window.geometry(
            f"{window_width}x{window_height}+{x}+{y}"
        )

        # =========================
        # HEADER
        # =========================

        header = tk.Frame(
            self.window,
            bg=PRIMARY,
            height=header_height
        )

        header.pack(fill="x")

        header.pack_propagate(False)

        title = tk.Label(
            header,
            text=f"🏨 CHECK IN PHÒNG {room.room_id}",
            font=title_font,
            bg=PRIMARY,
            fg=TEXT_WHITE
        )

        title.pack(expand=True)

        # =========================
        # MAIN CARD
        # =========================

        card = tk.Frame(
            self.window,
            bg=CARD_COLOR,
            padx=20,
            pady=15
        )

        card.pack(
            padx=20,
            pady=15,
            fill="both",
            expand=True
        )

        # =========================
        # FORM
        # =========================

        self.name_entry = self.create_input(
            card,
            "👤 Họ và tên",
            input_font
        )

        self.cccd_entry = self.create_input(
            card,
            "🪪 CCCD",
            input_font
        )

        self.phone_entry = self.create_input(
            card,
            "📞 Số điện thoại",
            input_font
        )

        self.checkin_entry = self.create_input(
            card,
            "📅 Ngày checkin (YYYY-MM-DD)",
            input_font
        )

        self.checkout_entry = self.create_input(
            card,
            "📅 Ngày checkout (YYYY-MM-DD)",
            input_font
        )

        # =========================
        # BUTTON AREA
        # =========================

        button_frame = tk.Frame(
            card,
            bg=CARD_COLOR
        )

        button_frame.pack(
            pady=15,
            fill="x"
        )

        confirm_btn = tk.Button(
            button_frame,
            text="✔ XÁC NHẬN CHECK IN",
            font=button_font,
            bg=SUCCESS,
            fg=TEXT_WHITE,
            relief="flat",
            cursor="hand2",
            height=2,
            command=self.submit
        )

        confirm_btn.pack(
            fill="x",
            pady=5
        )

       
        

        # =========================
        # HOVER EFFECT
        # =========================

        self.add_hover_effect(
            confirm_btn,
            SUCCESS,
            "#059669"
        )

     
        

    # =========================
    # CREATE INPUT
    # =========================

    def create_input(
        self,
        parent,
        label_text,
        input_font
    ):

        container = tk.Frame(
            parent,
            bg=CARD_COLOR
        )

        container.pack(
            fill="x",
            pady=6
        )

        label = tk.Label(
            container,
            text=label_text,
            font=("Arial", 11, "bold"),
            bg=CARD_COLOR,
            fg=TEXT_GRAY,
            anchor="w"
        )

        label.pack(
            fill="x",
            pady=(0, 5)
        )

        entry = tk.Entry(
            container,
            font=input_font,
            bg=INPUT_BG,
            fg=TEXT_WHITE,
            insertbackground=TEXT_WHITE,
            relief="flat",
            bd=0
        )

        entry.pack(
            fill="x",
            ipady=6
        )

        return entry

    # =========================
    # HOVER EFFECT
    # =========================

    def add_hover_effect(
        self,
        button,
        normal,
        hover
    ):

        button.bind(
            "<Enter>",
            lambda e: button.config(bg=hover)
        )

        button.bind(
            "<Leave>",
            lambda e: button.config(bg=normal)
        )

    # =========================
    # SUBMIT
    # =========================

    def submit(self):

        try:

            name = self.name_entry.get()

            cccd = self.cccd_entry.get()

            phone = self.phone_entry.get()

            checkin = self.checkin_entry.get()

            checkout = self.checkout_entry.get()

            self.booking_service.checkin(
                self.room,
                name,
                cccd,
                phone,
                checkin,
                checkout
            )

            messagebox.showinfo(
                "Thành công",
                "Check in thành công"
            )

            self.refresh_callback()

            self.window.destroy()

        except Exception as e:

            messagebox.showerror(
                "Lỗi",
                str(e)
            )