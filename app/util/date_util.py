from datetime import datetime

def str_to_hour_minute(str):
    if not str:
        raise ValueError("Please send a string")

    return datetime.strptime(str, '%H:%M')