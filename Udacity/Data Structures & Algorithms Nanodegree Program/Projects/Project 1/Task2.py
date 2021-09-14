"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

from typing import Tuple

def add_time(data: dict, phone: str, time: int):
    if phone in data:
        data[phone] += time
    else:
        data[phone] = time

def find_greatest(data: dict) -> Tuple[str, int]:

    phone_number = None
    phone_time = 0

    for phone in data:
        if data[phone] > phone_time:
            phone_time = data[phone]
            phone_number = phone

    return phone_number, phone_time

def print_longest_call():
    phone_data = {}

    for call in calls:
        call_time = int(call[3])
        add_time(phone_data, call[0], call_time)
        add_time(phone_data, call[1], call_time)

    phone, time = find_greatest(phone_data)

    print(f'{phone} spent the longest time, {time} seconds, on the phone during September 2016.')

print_longest_call()

