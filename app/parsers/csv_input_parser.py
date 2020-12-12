from app.parsers.calendar_input_parser import CalendarInputParser
from pathlib import Path
from app.cal.models import CalenderEntry
from app.util.date_util import str_to_hour_minute

import csv

class CSVCalendarInputParser(CalendarInputParser):

    def __init__(self, source_name):
        self.source_name = source_name

    def parse(self):
        base_path = Path(__file__).parent.parent
        file_name = "../data/%s.csv" % self.source_name
        calendar = []
        with open((base_path / file_name).resolve()) as f:
            for line in csv.reader(f):
                try:
                    entry = CalenderEntry(
                        line[0], line[1], str_to_hour_minute(line[2]), str_to_hour_minute(line[3])
                    )
                    calendar.append(entry)
                except IndexError:
                    # I assume that we wouldn't want to fail if one entry is problematic
                    pass

        return calendar
