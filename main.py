from app.cal.gong_calendar import Calendar
from app.parsers.csv_input_parser import CSVCalendarInputParser

import sys

if __name__ == '__main__':
    list = sys.argv
    file_name = "calendar" if len(list) < 2 else list[1]
    people = ["Alice", "Jack", "Bob"] if len(list) < 3 else list[2].split(",")
    cal = Calendar(CSVCalendarInputParser, file_name)
    cal.find_availability(
        people,
        1
    )