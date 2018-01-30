#SwollenNolon
#1/29/18
#adventure.py

print('You wake up in the middle of a desert.')
print('You look around you.')
print('To the north, if you squint, you can see a town.')
print('To the east, far away, there are tall, snow capped mountains.')
print('To the south, behind you, the land seems to stop suddenly. It might be a cliff.')
print('To the west, you can see a long, winding road, that goes past the horizon.')
print(' ')
print('Press 1 to go north, 2 to go east, 3 to go south, 4 to go west, and 5 to stay here.')
direc = int(input('Which way do you go?'))
if direc == 1:
    print(' ')
    print('You start walking to the north.')
    print('It takes almost a full day, and as the sun is setting, you stumble up to the gates.')
    print('There are guards standing at the gates.')
    print('They ask you what you\'re doing here.')
    print(' ')
    print('Press 1 to tell them the truth, that you don\'t know anything, press 2 to lie to them and say that you live in the town and are trying to get home, or press 3 to try to fight the guards and force your way through the gates.')
    town1 = input('What do you do?')
    if town1 == 1:
        print(' ')
        print('The guards don\'t believe your nonsense story. Being bayonetted is not a nice way to die.')
        print(' ')
        print('GAME OVER')
    if town1 == 2:
        print(' ')
        print('The guards are intimidating, but not all that intelligent. They let you inside the city.')
    if town1 == 3:
        print(' ')
        print('Your attempt to fight the guards doesn\'t end well, seeing as you haven\'t had any food for the whole day.')
        print('The guards take no nonsense. Being bayonetted is not a nice way to die.')
        print(' ')
        print('GAME OVER')
elif direc == 2:
    print('')
elif direc == 3:
    print('')
elif direc == 4:
    print('')
elif direc == 5:
    print('You die of starvation and of exposure to the elements.')
    print(' ')
    print('GAME OVER')
