import attr

@attr.s
class CalenderEntry:
    name = attr.ib()
    subject = attr.ib()
    start_time = attr.ib()
    end_time = attr.ib()
