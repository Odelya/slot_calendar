from app.cal.slot_calender import SlotCalender

class Calendar:

    def __init__(self, input_parser, source_name):
        self.input_parser = input_parser
        self.source_name = source_name

    def find_availability(self, names_list, duration_in_hours):
        calendar = self.input_parser(self.source_name).parse()
        slots = SlotCalender(calendar).find_available_slots(names_list, duration_in_hours)
        self.print_slots(slots)

    def print_slots(self, slots):
        for slot in slots:
            print("Availability slot at {:d}:{:02d}".format(slot.hour, slot.minute))
