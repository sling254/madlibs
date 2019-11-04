import string
import random

vowels = "aeiou"
consonant = "bcdefghjklmnpqrstyvwz"
letter= string.ascii_lowercase
letter_input_1 = raw_input(
    'choose a  letter ...."V" for a vowel, for a consonant choose "C" , for anyother letter choose "L": ')
letter_input_2 = raw_input(
    'choose a  letter ...."v" for a vowel, for a consonant choose "C" , for anyother letter choose "L": ')
letter_input_3 = raw_input(
    'choose a  letter ...."v" for a vowel, for a consonant choose "C" , for anyother letter choose "L": ')
letter_input_4 = raw_input(
    'choose a  letter ...."v" for a vowel, for a consonant choose "C" , for anyother letter choose "L": ')
letter_input_5 = raw_input(
    'choose a  letter ...."v" for a vowel, for a consonant choose "C" , for anyother letter choose "L": ')

def generator():

    # input no.1
    if letter_input_1 == V:
        letter1 = random.choice(vowels)
    elif letter_input_1 == C:
        letter1 = random.choice(consonant)
    elif letter1_input_1 == L:
        letter1 = random.choice(letter)
    else:
        letter1 = letter_input_1

    # input no.2
    if letter_input_2 == V:
        letter2 = random.choice(vowels)
    elif letter_input_2 == C:
        letter2 = random.choice(consonant)
    elif letter_input_2 == L:
        letter2 = random.choice(letter)
    else:
        letter2 = letter_input_2

    # input no.3
    if letter_input_3 == V:
        letter3 = random.choice(vowels)
    elif letter_input_3 == C:
        letter3 = random.choice(consonant)
    elif letter_input_3 == L:
        letter3 = random.choice(letter)
    else:
        letter3 = letter_input_3

    # input no. 4
    if letter_input_4 == V:
        letter4 = random.choice(vowels)
    elif letter_input_4 == C:
        letter4 = random.choice(consonant)
    elif letter_input_4 == L:
        letter4 = random.choice(letter)
    else:
        letter4 = letter_input_4

    # input no. 5
    if letter_input_5 == V:
        letter5 = random.choice(vowels)
    elif letter_input_5 == C:
        letter5 = random.choice(consonant)
    elif letter_input_5 == L:
        letter5 = random.choice(letter)
    else:
        letter5 = letter_input_5

    name = letter1+letter2+letter3+letter4+letter5

    return name

for babynames in range(20):

 generator()













