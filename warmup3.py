#SwollenNolon
#1/31/18
#warmup3.py

inte = int(input('Enter an integer: '))
if inte % 2 == 0 and inte % 3 == 0:
    print('It\'s divisible by both 2 and 3.')
elif inte % 2 == 0:
    print('It\'s divisible by 2 but not 3.')
elif inte % 3 == 0:
    print('It\'s divisible by 3 but not 2.')
else:
    print('It\'s divisible by neither 2 nor 3.')
