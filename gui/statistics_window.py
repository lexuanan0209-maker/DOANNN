from services.statistics_service import show_statistics


class StatisticsWindow:

    def __init__(self, rooms):

        show_statistics(rooms)