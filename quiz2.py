#IanNolon
#2/12/18
#quiz2.py

word1 = input('Enter a word: ')
word2 = input('Enter another word: ')

if len(word1) == len(word2):
    print('The words are the same length')
elif len(word1) > len(word2):
    print('The first word is longer.')
elif len(word1) < len(word2):
    print('The second word is longer.')

if 'p' in word1 and 'p' in word2:
    print('Both words have a p')
elif 'p' in word1:
    print('Only the first word has a p')
elif 'p' in word2:
    print('Only the second word has a p')
else:
    print('Neither word has a p')

num1 = int(input('Number 1: '))
num2 = int(input('Number 2: '))
if num1 + num2 == 12:
    print('Correct')
else:
    print('Incorrect')
