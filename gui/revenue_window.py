import tkinter as tk
from datetime import datetime

from utils.file_handler import load_json

BOOKING_FILE = "data/bookings.json"


class RevenueWindow:

    def __init__(self):

        self.window = tk.Toplevel()

        self.window.title("THỐNG KÊ DOANH THU")

        self.window.geometry("700x500")

        self.window.configure(bg="#181A1F")

        # =========================================================================
        # ĐĂNG KÝ SỰ KIỆN ĐÓNG CỬ SỔ: Khi nhấn nút X sẽ gọi hàm self.on_close để dọn dẹp
        # =========================================================================
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

        now = datetime.now()

        self.current_month = now.month

        self.current_year = now.year

        title = tk.Label(
            self.window,
            text="📈 THỐNG KÊ DOANH THU",
            font=("Arial", 24, "bold"),
            bg="#181A1F",
            fg="white"
        )

        title.pack(pady=20)

        # =========================
        # MONTH CONTROL
        # =========================

        top_frame = tk.Frame(
            self.window,
            bg="#181A1F"
        )

        top_frame.pack(pady=10)

        prev_btn = tk.Button(
            top_frame,
            text="⬅",
            font=("Arial", 14, "bold"),
            width=5,
            bg="#374151",
            fg="white",
            relief="flat",
            command=self.prev_month
        )

        prev_btn.pack(side="left", padx=10)

        self.month_label = tk.Label(
            top_frame,
            text="",
            font=("Arial", 18, "bold"),
            bg="#181A1F",
            fg="#22C55E"
        )

        self.month_label.pack(side="left", padx=20)

        next_btn = tk.Button(
            top_frame,
            text="➡",
            font=("Arial", 14, "bold"),
            width=5,
            bg="#374151",
            fg="white",
            relief="flat",
            command=self.next_month
        )

        next_btn.pack(side="left", padx=10)

        # =========================
        # REVENUE CARD
        # =========================

        self.revenue_card = tk.Frame(
            self.window,
            bg="#2563EB",
            padx=40,
            pady=40
        )

        self.revenue_card.pack(
            pady=40
        )

        self.revenue_label = tk.Label(
            self.revenue_card,
            text="",
            font=("Arial", 26, "bold"),
            bg="#2563EB",
            fg="white"
        )

        self.revenue_label.pack()

        # =========================
        # TABLE
        # =========================

        self.listbox = tk.Listbox(
            self.window,
            width=80,
            height=12,
            font=("Arial", 12),
            bg="#1F2937",
            fg="white",
            bd=0
        )

        self.listbox.pack(padx=20, pady=10)

        self.update_revenue()

    def update_revenue(self):

        self.month_label.config(
            text=f"THÁNG {self.current_month} / {self.current_year}"
        )

        bookings = load_json(
            BOOKING_FILE
        )

        total = 0

        self.listbox.delete(0, tk.END)

        for booking in bookings:

            if (
                booking.get("status")
                ==
                "Đã thanh toán"
            ):

                checkout_date = datetime.strptime(
                    booking["checkout"],
                    "%Y-%m-%d"
                )

                if (
                    checkout_date.month
                    ==
                    self.current_month
                    and
                    checkout_date.year
                    ==
                    self.current_year
                ):

                    price = booking.get(
                        "total_price",
                        0
                    )

                    total += price

                    self.listbox.insert(
                        tk.END,
                        (
                            f"Phòng {booking['room_id']}  |  "
                            f"{booking['customer']['name']}  |  "
                            f"{price:,} VNĐ"
                        )
                    )

        self.revenue_label.config(
            text=f"{total:,} VNĐ"
        )

    def prev_month(self):

        self.current_month -= 1

        if self.current_month < 1:

            self.current_month = 12

            self.current_year -= 1

        self.update_revenue()

    def next_month(self):

        self.current_month += 1

        if self.current_month > 12:

            self.current_month = 1

            self.current_year += 1

        self.update_revenue()

    # =========================================================================
    # HÀM ON_CLOSE: Hủy các lịch trình chạy ngầm trước khi chính thức giải phóng cửa sổ
    # =========================================================================
    def on_close(self):
        try:
            # Tìm và hủy tất cả các lệnh "after" của Tkinter đang chờ chạy trên cửa sổ này
            for after_id in self.window.eval('after info').split():
                self.window.after_cancel(after_id)
        except Exception:
            pass
        
        # Hủy hoàn toàn widget cửa sổ
        self.window.destroy()