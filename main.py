
from gui.login_window import LoginWindow
from gui.app import HotelApp


if __name__ == "__main__":

    login = LoginWindow()

    user = login.run()

    if user:

        app = HotelApp(user)

        app.run()

