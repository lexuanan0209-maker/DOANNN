
from utils.file_handler import load_json


USER_FILE = "auth/user.json"


class AuthService:

    def __init__(self):

        self.users = load_json(USER_FILE)

    def login(self, username, password):

        for user in self.users:

            if (
                user["username"] == username
                and
                user["password"] == password
            ):

                return user

        return None

