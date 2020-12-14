from app.util.date_util import str_to_hour_minute
from datetime import timedelta

START_HOUR = str_to_hour_minute("07:00")
END_HOUR = str_to_hour_minute("19:00")

class SlotCalender:

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
        The algorithm compares the latest meeting time with the next pair ending meeting time and uses the max
        to continue iterating and find the next available meeting.
        RESTRICTION: we will return the first available slot in a time window of a few hours.
        If the first available slot is at 13:00 and the next meeting is that 15:00 we will return 13:00, while
        every minute from 13:00 to 14:00 is actually available.
        :param names_list: list of names. Should match the name in the cal list. e.g. ["Bob", "Alice"]
        :param event_duration_in_hours: duration of the event. e g 1 for 1 hour.
        :return: list of available slots in datetime format.
        """
        duration = timedelta(hours=event_duration_in_hours)
        busy_slots = self.get_busy_slots_for_names_list(names_list)
        pairs = self.get_sort_busy_slots(busy_slots)
        available_slots = []
        latest_busy_time = START_HOUR
        i = 0
        while latest_busy_time <= END_HOUR and i < len(pairs) - 1:
            start_next_meeting = pairs[i+1][0]
            if latest_busy_time + duration <= start_next_meeting:
                available_slots.append(latest_busy_time)

            latest_busy_time = max(pairs[i+1][1], latest_busy_time)
            i += 1

        return available_slots

    def get_busy_slots_for_names_list(self, names_list):
        return [(line.start_time, line.end_time) for line in self.calender_lines if line.name in set(names_list)]

    def get_sort_busy_slots(self, slots):
        return sorted([(START_HOUR, START_HOUR)] + slots + [(END_HOUR, END_HOUR)])
