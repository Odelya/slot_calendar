from app.util.date_util import str_to_hour_minute
from datetime import timedelta

class SlotCalender:

    START_HOUR = str_to_hour_minute("07:00")
    END_HOUR = str_to_hour_minute("19:00")

    def __init__(self, calendar_lines):
        """
        :param calendar_lines: list of Calender model
        """
        self.calender_lines = calendar_lines

    def find_available_slots(self, names_list, event_duration_in_hours):
        """
        The method loops over the cal lines and find the available slots for the required people
        to attend it in names_list.
        The algorithm filters out slots that are not in the name list, then creates a new list of tuples
        with start and end hours, and sorts it for iteration.
        while iterating we compare the end time with the beginning time of the next slot to find an available
        hour.
        :param names_list: list of names. Should match the name in the cal list. e.g. ["Bob", "Alice"]
        :param event_duration_in_hours: duration of the event. e g 1 for 1 hour.
        :return: list of available slots in datetime format.
        """
        duration = timedelta(hours=event_duration_in_hours)
        busy_slots = self.get_busy_slots_for_names_list(names_list)
        sorted_busy_slots = self.get_sort_busy_slots(busy_slots)

        available_slots = []
        for start, end in self.prepare_pairs_to_compare(sorted_busy_slots):
            while start + duration <= end:
                available_slots.append(start)
                start += duration

        return available_slots

    def get_busy_slots_for_names_list(self, names_list):
        return [(line.start_time, line.end_time) for line in self.calender_lines if line.name in set(names_list)]

    def get_sort_busy_slots(self, slots):
        return sorted([(self.START_HOUR, self.START_HOUR)] + slots + [(self.END_HOUR, self.END_HOUR)])

    def prepare_pairs_to_compare(self, slots):
        return ((slots[i][1], slots[i + 1][0]) for i in range(len(slots) - 1))