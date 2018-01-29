#SwollenNolon
#1/29/18
#unitConvertor.py

print('Choose an option!')
print('1) Kilometers to Miles')
print('2) Kilograms to Pounds')
print('3) Liters to Gallons')
print('4) Celsius to Fahrenheit')
choice = int(input('Which one?'))
if (choice == 1):
    km = float(input('Enter Kilometers'))
    print (km * 0.621371)
elif (choice == 2):
    kg = float(input('Enter Kilograms'))
    print (kg * 2.20462)
elif (choice == 3):
    liters = float(input('Enter Liters'))
    print (liters * 0.264172)
elif (choice == 4):
    cel = float(input('Enter Degrees in Celsius'))
    print (cel * 1.8 + 32)
else:
    print ('Error')
