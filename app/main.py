from app.cal.gong_calendar import Calendar
from app.parsers.csv_input_parser import CSVCalendarInputParser

if __name__ == '__main__':
    cal = Calendar(CSVCalendarInputParser, "calendar")
    cal.find_availability(
        ["Alice", "Jack", "Bob"],
        1
    )