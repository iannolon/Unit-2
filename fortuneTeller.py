#SwollenNolon
#1/29/18
#fortuneTeller.py

color = input('Pick red or blue:')
number = int(input('Pick a number from 1-4:'))
if (color == 'red' and number == 1):
    print ('You will find an 100 dollar bill lying in the street within the next week.')
elif (color == 'red' and number == 2):
    print ('You will fall off of a canoe into a mud hole and your best friend will die saving you.')
elif (color == 'red' and number == 3):
    print ('You will learn to play the oboe.')
elif (color == 'red' and number == 4):
    print ('You will discover a new species of insect.')
elif (color == 'blue' and number == 1):
    print ('You will hike Mount Everest for free.')
elif (color == 'blue' and number == 2):
    print ('You will be the pioneer of the next gold rush and get filthy rich.')
elif (color == 'blue' and number == 3):
    print ('You will find that somebody deposited 1000 bitcoins into your account in 2013 when they weren\'t worth anything and now you\re loaded.')
elif (color == 'blue' and number == 4):
    print ('You will get AIDS because you cut your hand and somebody\'s blood got in it')
else:
    print('Error')
