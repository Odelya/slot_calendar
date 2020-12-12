from app.cal.slot_calender import SlotCalender
from app.cal.models import CalenderEntry
from app.util.date_util import str_to_hour_minute

def test_it_should_return_slots_for_person_names():
    calender_lines = [
        CalenderEntry(name="Alice", subject="test 1", start_time=str_to_hour_minute("10:00"), end_time=str_to_hour_minute("12:00")),
        CalenderEntry(name="Alice", subject="test 1", start_time=str_to_hour_minute("15:00"), end_time=str_to_hour_minute("16:00")),
        CalenderEntry(name="John", subject="test 1", start_time=str_to_hour_minute("16:00"), end_time=str_to_hour_minute("19:00"))
    ]
    slots = SlotCalender(calender_lines).find_available_slots(["Alice", "John"], event_duration_in_hours=1)
    result = ["{:d}:{:02d}".format(slot.hour, slot.minute) for slot in slots]
    expected = ['7:00', '8:00', '9:00', '12:00', '13:00', '14:00']
    assert result == expected

def test_it_should_return_nothing_if_none_are_available():
    calender_lines = [
        CalenderEntry(name="Alice", subject="test 1", start_time=str_to_hour_minute("7:00"),
                      end_time=str_to_hour_minute("19:00")),
    ]
    slots = SlotCalender(calender_lines).find_available_slots(["Alice", "John"], event_duration_in_hours=1)
    result = ["{:d}:{:02d}".format(slot.hour, slot.minute) for slot in slots]
    expected = []
    assert result == expected
