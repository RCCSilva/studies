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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

import re

## Part A

def define_type(phone: str) -> str:
  if phone[0] == '(':
    return 'fixed'

  if phone[5] == ' ' and phone[0] in {'7', '8', '9'}:
    return 'mobile'

  if phone[:3] == '140':
    return 'telemarketers'
  
  raise Exception(f'Failed to determine type of {phone}')

def get_area_code(phone: str) -> str:
  return re.search(r'\(\d+\)', phone).group(0)

def get_mobile_prefixes(phone: str) -> str:
  return phone[:4]

def is_bangalore(phone: str) -> bool:
  return phone[:5] == '(080)'

def print_numbers_called_by_bangalore():
  numbers = set()

  for call in calls:
    if is_bangalore(call[0]):

      phone_called = call[1]
      code = None

      type_ = define_type(phone_called)

      if type_ == 'fixed':
        code = get_area_code(phone_called)
      elif type_ == 'mobile':
        code = get_mobile_prefixes(phone_called)
      
      if code:
        numbers.add(code)

  numbers = sorted(numbers)

  numbers_print = '\n'.join(numbers)

  print(f'The numbers called by people in Bangalore have codes:\n{numbers_print}')

print_numbers_called_by_bangalore()

## Part B

def print_percentage_called_bangalore():
  bangalore_from = 0
  bangalore_to = 0

  for call in calls:
    if is_bangalore(call[0]):

      bangalore_from += 1

      phone_called = call[1]

      type_ = define_type(phone_called)

      if type_ == 'fixed' and is_bangalore(phone_called):
        bangalore_to += 1

  percentage = bangalore_to / bangalore_from

  print(f'{percentage:.2%} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.')

print_percentage_called_bangalore()

