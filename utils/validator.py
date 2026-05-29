
from datetime import datetime

from exceptions.custom_exceptions import (
    InvalidDateError
)


def validate_date(checkin, checkout):

    d1 = datetime.strptime(
        checkin,
        "%Y-%m-%d"
    )

    d2 = datetime.strptime(
        checkout,
        "%Y-%m-%d"
    )

    if d2 <= d1:

        raise InvalidDateError(
            "Ngày checkout phải lớn hơn checkin"
        )

