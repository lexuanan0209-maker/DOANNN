
class Customer:

    def __init__(
        self,
        name,
        cccd,
        phone
    ):

        self.name = name
        self.cccd = cccd
        self.phone = phone

    def to_dict(self):

        return {

            "name": self.name,

            "cccd": self.cccd,

            "phone": self.phone
        }

