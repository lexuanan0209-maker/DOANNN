
import customtkinter as ctk

from tkinter import messagebox

from services.auth_service import AuthService


class LoginWindow:

    def __init__(self):

        self.auth_service = AuthService()

        self.user = None

        self.root = ctk.CTk()

        self.root.geometry("400x400")

        self.root.title("LOGIN")

        title = ctk.CTkLabel(

            self.root,

            text="HOTEL LOGIN",

            font=("Arial", 28, "bold")
        )

        title.pack(pady=30)

        self.username = ctk.CTkEntry(

            self.root,

            placeholder_text="Username",

            height=45
        )

        self.username.pack(

            padx=30,
            pady=15,
            fill="x"
        )

        self.password = ctk.CTkEntry(

            self.root,

            placeholder_text="Password",

            show="*",

            height=45
        )

        self.password.pack(

            padx=30,
            pady=15,
            fill="x"
        )

        login_btn = ctk.CTkButton(

            self.root,

            text="LOGIN",

            height=50,

            command=self.login
        )

        login_btn.pack(

            padx=30,
            pady=30,
            fill="x"
        )

    def login(self):

        username = self.username.get()

        password = self.password.get()

        user = self.auth_service.login(
            username,
            password
        )

        if user:

            self.user = user

            self.root.destroy()

        else:

            messagebox.showerror(
                "Error",
                "Sai tài khoản hoặc mật khẩu"
            )

    def run(self):

        self.root.mainloop()

        return self.user
