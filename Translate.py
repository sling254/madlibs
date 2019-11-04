

def translate(Phrase):
    translation = ""
    for letter in Phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                 translation= translation+ "G"
            else:
                 translation = translation+ "g"
        else:
            translation = translation+ letter

    return translation

print translate((raw_input("enter a phrase: ")))