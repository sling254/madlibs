Secret_word = "letter E"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
print ("RIDDLE RIDDLE !")
print ("I am the first on EARTH")
print ("I am the second in HEAVEN")
print ("I appear twice in a WEEK")
print ("You can only see me once in a YEAR")
print ("Although am in the middle of the SEA")
print ("But i never appear in a DAY")

while guess != Secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = raw_input("Who Am I: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print ("Out of Guesses, YOU LOSE!")
else:
    print("You win!")
