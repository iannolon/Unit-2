#SwollenNolon
#1/24/18
#ageCalculator.py

from datetime import date
byear = int(input('What year were you born?'))
bmonth = int(input('What month were you born?'))
bday = int(input ('What day were you born?'))

dayage = (date.today().year - byear) * 365 + (date.today().month - bmonth) * 30 + (date.today().day - bday )
age = dayage//365
print('You are',age,'years old.')
if date.today().day == bday:
    print('Happy Birthday!')
