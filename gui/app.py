import tkinter as tk
from tkinter import messagebox
from datetime import datetime

from services.room_service import RoomService
from services.booking_service import BookingService

from gui.room_grid import RoomGrid
from gui.checkin_window import CheckinWindow
from gui.checkout_window import CheckoutWindow
from gui.statistics_window import StatisticsWindow
from gui.revenue_window import RevenueWindow

# =========================
# COLORS
# =========================

BG_COLOR = "#181A1F"
SIDEBAR_COLOR = "#111827"

PRIMARY = "#2563EB"
SUCCESS = "#10B981"
WARNING = "#F59E0B"
DANGER = "#DC2626"

TEXT_WHITE = "white"


class HotelApp:

    def __init__(self, current_user=None):

        self.current_user = current_user

        self.root = tk.Tk()

        self.root.title("HOTEL MANAGEMENT SYSTEM")

        self.root.geometry("1400x850")

        self.root.minsize(1200, 700)

        self.root.configure(bg=BG_COLOR)

        self.root.protocol(
            "WM_DELETE_WINDOW",
            self.on_close
        )

        # self.root.iconbitmap("assets/hotel.ico")

        self.room_service = RoomService()

        self.booking_service = BookingService(
            self.room_service
        )

        # =========================
        # SIDEBAR
        # =========================

        self.sidebar = tk.Frame(
            self.root,
            bg=SIDEBAR_COLOR,
            width=220
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        self.sidebar.pack_propagate(False)

        logo = tk.Label(
            self.sidebar,
            text="🏨 HOTEL",
            font=("Arial", 28, "bold"),
            fg=TEXT_WHITE,
            bg=SIDEBAR_COLOR
        )

        logo.pack(pady=40)

        if self.current_user:

            role_label = tk.Label(
                self.sidebar,
                text=(
                    f"{self.current_user['username']}\n"
                    f"({self.current_user['role']})"
                ),
                font=("Arial", 12, "bold"),
                fg="#22C55E",
                bg=SIDEBAR_COLOR
            )

            role_label.pack(pady=10)

        # =========================
        # BUTTONS
        # =========================

        btn_refresh = self.create_sidebar_button(
            "🔄 Làm mới",
            PRIMARY,
            self.refresh_grid
        )

        btn_refresh.pack(
            pady=15,
            padx=20,
            fill="x"
        )

        self.add_hover_effect(
            btn_refresh,
            PRIMARY,
            "#1D4ED8"
        )

        if (
            self.current_user
            and
            self.current_user["role"] == "admin"
        ):

            btn_statistics = self.create_sidebar_button(
                "📊 Thống kê",
                WARNING,
                self.show_statistics
            )

            btn_statistics.pack(
                pady=15,
                padx=20,
                fill="x"
            )

            self.add_hover_effect(
                btn_statistics,
                WARNING,
                "#D97706"
            )

            btn_revenue = self.create_sidebar_button(
                "💰 Doanh thu",
                SUCCESS,
                self.show_revenue
            )

            btn_revenue.pack(
                pady=15,
                padx=20,
                fill="x"
            )

            self.add_hover_effect(
                btn_revenue,
                SUCCESS,
                "#059669"
            )

        btn_exit = self.create_sidebar_button(
            "❌ Thoát",
            DANGER,
            self.on_close
        )

        btn_exit.pack(
            side="bottom",
            pady=30,
            padx=20,
            fill="x"
        )

        self.add_hover_effect(
            btn_exit,
            DANGER,
            "#B91C1C"
        )

        # =========================
        # MAIN CONTENT
        # =========================

        self.main_content = tk.Frame(
            self.root,
            bg=BG_COLOR
        )

        self.main_content.pack(
            side="right",
            fill="both",
            expand=True
        )

        # =========================
        # HEADER
        # =========================

        header = tk.Frame(
            self.main_content,
            bg=BG_COLOR,
            height=120
        )

        header.pack(
            fill="x",
            pady=20
        )

        title = tk.Label(
            header,
            text="HOTEL MANAGEMENT DASHBOARD",
            font=("Arial", 28, "bold"),
            fg=TEXT_WHITE,
            bg=BG_COLOR
        )

        title.pack(
            side="left",
            padx=30
        )

        # CLOCK

        self.clock_label = tk.Label(
            header,
            font=("Arial", 12, "bold"),
            fg=TEXT_WHITE,
            bg=BG_COLOR
        )

        self.clock_label.pack(
            side="right",
            padx=20
        )

        total_rooms = len(
            self.room_service.rooms
        )

        empty_rooms = len([
            room for room in self.room_service.rooms
            if room.status == "Trống"
        ])

        info_card = tk.Frame(
            header,
            bg=PRIMARY,
            padx=20,
            pady=15
        )

        info_card.pack(
            side="right",
            padx=30
        )

        self.info_label = tk.Label(
            info_card,
            text=(
                f"Tổng phòng: {total_rooms}\n"
                f"Phòng trống: {empty_rooms}"
            ),
            font=("Arial", 14, "bold"),
            fg=TEXT_WHITE,
            bg=PRIMARY
        )

        self.info_label.pack()

        # =========================
        # ROOM AREA
        # =========================

        self.grid_container = tk.Frame(
            self.main_content,
            bg=BG_COLOR
        )

        self.grid_container.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        self.canvas = tk.Canvas(
            self.grid_container,
            bg=BG_COLOR,
            highlightthickness=0
        )

        scrollbar = tk.Scrollbar(
            self.grid_container,
            orient="vertical",
            command=self.canvas.yview
        )

        self.grid_frame = tk.Frame(
            self.canvas,
            bg=BG_COLOR
        )

        self.grid_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window(
            (0, 0),
            window=self.grid_frame,
            anchor="nw"
        )

        self.canvas.configure(
            yscrollcommand=scrollbar.set
        )

        self.canvas.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        # =========================
        # MOUSE SCROLL
        # =========================

        self.canvas.bind_all(
            "<MouseWheel>",
            lambda e: self.canvas.yview_scroll(
                int(-1 * (e.delta / 120)),
                "units"
            )
        )

        # =========================
        # STATUS BAR
        # =========================

        self.status_bar = tk.Label(
            self.root,
            text="Hệ thống đang hoạt động",
            anchor="w",
            bg="#0F172A",
            fg=TEXT_WHITE
        )

        self.status_bar.pack(
            side="bottom",
            fill="x"
        )

        self.update_clock()

        self.refresh_grid()

    # =========================
    # CREATE BUTTON
    # =========================

    def create_sidebar_button(
        self,
        text,
        color,
        command
    ):

        return tk.Button(
            self.sidebar,
            text=text,
            font=("Arial", 12, "bold"),
            bg=color,
            fg=TEXT_WHITE,
            relief="flat",
            height=2,
            cursor="hand2",
            command=command
        )

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
    # CLOCK
    # =========================

    def update_clock(self):

        current_time = datetime.now().strftime(
            "%d/%m/%Y\n%H:%M:%S"
        )

        self.clock_label.config(
            text=current_time
        )

        self.root.after(
            1000,
            self.update_clock
        )

    
# =========================
# REFRESH GRID
# =========================

    def refresh_grid(self):

        self.update_dashboard()

    # LOADING CURSOR
        self.root.config(cursor="watch")

        self.root.update()

    # XÓA GRID CŨ
        for widget in self.grid_frame.winfo_children():

            widget.destroy()

        room_grid = RoomGrid(

            self.grid_frame,

            self.room_service.rooms,

            self.room_click,

            self.room_service,

            self.refresh_grid,

            self.current_user
    )

        room_grid.draw()

        self.root.config(cursor="")



    # =========================
    # UPDATE DASHBOARD
    # =========================

    def update_dashboard(self):

        total_rooms = len(
            self.room_service.rooms
        )

        empty_rooms = len([
            room for room in self.room_service.rooms
            if room.status == "Trống"
        ])

        self.info_label.config(
            text=(
                f"Tổng phòng: {total_rooms}\n"
                f"Phòng trống: {empty_rooms}"
            )
        )

    # =========================
    # ROOM CLICK
    # =========================

    def room_click(self, room):

        if room.status == "Trống":

            CheckinWindow(
                room,
                self.booking_service,
                self.refresh_grid
            )

        elif room.status == "Đang ở":

            CheckoutWindow(
                room,
                self.booking_service,
                self.refresh_grid
            )

        else:

            messagebox.showwarning(
                "Thông báo",
                "Phòng hiện không khả dụng"
            )

    # =========================
    # STATISTICS
    # =========================

    def show_statistics(self):

        StatisticsWindow(
            self.room_service.rooms
        )

    # =========================
    # REVENUE
    # =========================

    def show_revenue(self):

        RevenueWindow()

    # =========================
    # CLOSE APP
    # =========================

    def on_close(self):

        confirm = messagebox.askyesno(
            "Thoát",
            "Bạn có chắc muốn thoát?"
        )

        if confirm:
            self.root.destroy()

    # =========================
    # RUN APP
    # =========================

    def run(self):

        self.root.mainloop()