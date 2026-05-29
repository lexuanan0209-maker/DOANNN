
import matplotlib.pyplot as plt


def show_statistics(rooms):

    empty_rooms = 0

    busy_rooms = 0

    for room in rooms:

        if room.status == "Trống":

            empty_rooms += 1

        else:

            busy_rooms += 1

    labels = [
        "Trống",
        "Đang sử dụng"
    ]

    values = [
        empty_rooms,
        busy_rooms
    ]

    plt.figure(figsize=(6, 6))

    plt.pie(
        values,
        labels=labels,
        autopct='%1.1f%%'
    )

    plt.title(
        "HIỆU SUẤT SỬ DỤNG PHÒNG"
    )

    plt.show()

