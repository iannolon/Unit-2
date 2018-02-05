#SwollenNolon
#1/29/18
#adventure.py

print('You wake up in the middle of a desert. You look around you. To the north, if you squint, you can see a town. To the east, far away, there are tall, snow capped mountains. To the south, behind you, the land seems to stop suddenly. It might be a cliff. To the west, you can see a long, winding road, that goes past the horizon.')
print(' ')
print('Press 1 to go north, 2 to go east, 3 to go south, 4 to go west, and 5 to stay here.')
direc = int(input('Which way do you go?'))
if direc == 1:
    print(' ')
    print('You start walking to the north. It takes almost a full day, and as the sun is setting, you stumble up to the gates. There are guards standing at the gates.')
    print('They ask you what you\'re doing here.')
    print(' ')
    print('Press 1 to tell them the truth, that you don\'t know anything, press 2 to lie to them and say that you live in the town and are trying to get home, or press 3 to try to fight the guards and force your way through the gates.')
    town1 = int(input('What do you do?'))
    if town1 == 1:
        print(' ')
        print('The guards don\'t believe your nonsense story. Being bayonetted is not a nice way to die.')
        print(' ')
        print('GAME OVER')
    elif town1 == 2:
        print(' ')
        print('The guards are intimidating, but not all that intelligent. They let you inside the city.')
        print('This path is incomplete. Sorry.')
    elif town1 == 3:
        print(' ')
        print('Your attempt to fight the guards doesn\'t end well, seeing as you haven\'t had any food for the whole day. The guards take no nonsense. Being bayonetted is not a nice way to die.')
        print(' ')
        print('GAME OVER')
    else:
        print('Error')
elif direc == 2:
    print('You start walking to the east. You finally reach the mountains and start climbing up them. You find a cave entrance.')
    print(' ')
    print('Press 1 to go in the cave and 2 to continue up the mountain.')
    moun1 = int(input('Do you go in?'))
    if moun1 == 1:
        print(' ')
        print('You enter the cave. It\'s not nighttime yet, so there\'s some residual light from the outside. At first glance, the cave seems normal. But when you investigate further, it looks like there\'s a suspicious bump on the floor.')
        print(' ')
        print('Press 1 to try to find out what it is, press 2 to spend the night in the cave without investigating the bump, or press 3 to leave the cave.')
        cave1 = int(input('What do you do?'))
        if cave1 == 1:
            print('This path is incomplete. Sorry. ')
        elif cave1 == 2:
            print(' ')
            print('Despite your curiosity, you sleep in the cave for the night. You wake to see a snarling tiger in front of you. He\'s not happy to find you in his home.')
            print(' ')
            print('GAME OVER')
        elif cave1 == 3:
            print(' ')
            print('You continue up the mountain. You don\'t come across any other caves and your only option is to sleep without cover on the mountainside. You wake up without any limbs. You see scavengers running away with your legs sticking out of their backpacks. You die of starvation and exposure.')
            print(' ')
            print('GAME OVER')
        else:
            print('Error')
    elif moun1 == 2:
        print(' ')
        print('You continue up the mountain. You don\'t come across any other caves and your only option is to sleep without cover on the mountainside. You wake up without any limbs. You see scavengers running away with your legs sticking out of their backpacks. You die of starvation and exposure.')
        print(' ')
        print('GAME OVER')
    else:
        print('Error')
elif direc == 3:
    print('You start walking to the south. However, night falls before you are able to get to the cliff.')
    print(' ')
    print('Press 1 to try to find shelter and 2 to keep walking.')
    cliff1 = int(input('What do you do?'))
    if cliff1 == 1:
        print(' ')
        print('There isn\'t shelter in a desert. Your attempts to find a place to sleep are futile and you end up falling asleep in the middle of the desert. Your body is picked apart by the vultures.')
        print(' ')
        print('GAME OVER')
    elif cliff1 == 2:
        print(' ')
        print('Almost falling over from exhaustion, you finally reach the cliff. It\'s almost a mile wide and you can\'t see the bottom. To each side of you the cliff stretches on forever. On the other side of the cliff, you can see the foreboding desert become replaced by a lush forest, filled with plentiful fauna and flora. Press 1 to head back to where you were dropped off, press 2 to try to walk around the cliff, or press 3 to stay here to see if there\'s a way to get to the forest.')
        cliff2 = int(input('What do you do?'))
        if cliff2 == 1:
            print('You haven\'t slept or eaten anything in more than a day. Your body isn\'t able to walk the distance back to your starting position. Your last breath is of you gasping for breath in the middle of an unknown desert, your lungs filled with sand and your stomach empty of sustenence.')
            print(' ')
            print('GAME OVER')
        elif cliff2 == 2:
            print('You haven\'t slept or eaten anything in more than a day. Your body isn\'t able to walk the distance back around the canyon, and the end of the canyon is still nowhere in sight. Your last breath is of you gasping for breath in the middle of an unknown desert, your lungs filled with sand and your stomach empty of sustenence.')
        elif cliff2 == 3:
            print('There seems to be climbing equimpent, a grappling hook, and some rope on the side of the cliff. Looks like some earlier travelers didn\'t have good luck. You gather up the equipment and begin the climb down. 50 feet below the desert, you place pick after pick on the side of the canyon. You wonder how you know how to climb. Suddenly, it dawns on you. All of your memories come flooding back to you. Oh, the cruelty! How could they have taken away all of your memories? But just as your memories come back to you, you feel debris trickling down from above as your pick becomes dislodged from the cliff. As the floor of the canyon rises up to meet you, you whisper "I\'m sorry" to everybody you let down by failing.')
            print(' ')
            print('GAME OVER')
        else:
            print('Error')
    else:
        print('Error')
elif direc == 4:
    print('This path is incomplete. Sorry.')
elif direc == 5:
    print('You die of starvation and of exposure to the elements.')
    print(' ')
    print('GAME OVER')
else:
    print('Error')
