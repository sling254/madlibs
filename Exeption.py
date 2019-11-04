

try:
    number= int(raw_input("Enter a number: "))
except ValueError as err:

    print (err)
