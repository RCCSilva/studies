"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

phones_set = set()

def print_unique_phone_numbers():
    for i in range(len(texts)):
        phones_set.add(texts[i][0])
        phones_set.add(texts[i][1])

    for i in range(len(calls)):
        phones_set.add(calls[i][0])
        phones_set.add(calls[i][1])

    print(f'There are {len(phones_set)} different telephone numbers in the records.')

print_unique_phone_numbers()

