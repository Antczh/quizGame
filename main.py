print('Welcome to my quiz!')

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Ok, lets play!")

answer = input("What is the name of the pub at the entrance to Diagon Alley? ")
if answer == "The Leaky Cauldron" or answer == "Leaky Cauldron": 
    print('Correct!')
else: 
    print("Incorrect")